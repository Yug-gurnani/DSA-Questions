"""Given an array of integers and a sum B, find all unique combinations in the array where the sum is equal to B.
The same number may be chosen from the array any number of times to make B.

Note:
        1. All numbers will be positive integers.
        2. Elements in a combination (a1, a2, …, ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
        3. The combinations themselves must be sorted in ascending order.


Backtracking
Sort candidates first to increase efficiency bc if 
current candidate is greated than target, the elements
after current is also larger than target because the 
array is sorted so we can terminate at current to reduce 
the time
Intuitive: we could incrementally build the combination, 
and once we find the current combination is not valid, 
we backtrack and try another option
1) Base case recursion: 
- If remain == 0: we find one target sum, then we add current 
combination to final list
- If currentNum > remain: which will cause to exceed the target
value, we will not explore this path
2) Other than above cases, we continue to explore the sublist 
of candidates as [index ... n]. 
For each of the candidate, we invoke the recursive function itself 
with updated parameters.
-we add the current candidate into the combination.
-With the added candidate, we now have less sum to fulfill, 
EX: remain - candidate
-For the next exploration, still we start from the current cursor
index
-At the end of each exploration, we backtrack by popping out the
candidate out of the combination

    EX:  [3,4,5] target=8   [[3,5],[3,4]]
                     []
          [3]        [4]        [5]
    [3,3][3,4][3,5]  [4,4][4,5] [5,5]
 [3,3,3][3,4,4] 
(too big)(too big)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def backtrack(index, path, remain):
            # condition to terminate:
            # 1) find the right candidate 
            # 2) candidate is larger than target
            # reach the leaf of the tree
            if remain == 0:
                output.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if remain - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtrack(i, path, remain - candidates[i])
                path.pop()
        backtrack(0, [], target)
 
        return output  
        # Note: there might be duplicate answers ex: [2, 2, 3], [3, 2, 2]
        # time: O(N^target)
        # each recursive step we go over all existing candidates, so base N
        # go as deep as target in our recursive calls (if candidates are close to 1), 
        # so power of target