"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

same as combination sum 1 but we have to skip same elements which we do by sorting and checking the next valid number
"""
def combinationSum2(self, arr: List[int], t: int) -> List[List[int]]:
    res = []
    temp = []
    n = len(arr)
    arr.sort()
    def backtrack(arr,t,temp,res,curr):

        if t == 0:
            res.append(temp[:])
            return
        if t < 0:
            return
        for next_curr in range(curr,len(arr)):
            if next_curr > curr and arr[next_curr] == arr[next_curr-1]:
                continue
            pick = arr[next_curr]
            
            temp.append(pick)
            backtrack(arr,t-pick,temp,res,next_curr+1)
                
            temp.pop()
    backtrack(arr,t,temp,res,0)
    return res
"""
TC = o(2^n)
SC = o(1)
"""