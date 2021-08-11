"""
Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
Example 1:

Input:
K = 3
arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation:Above test case has 3 sorted
arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],[4, 5, 6], 
[7, 8, 9]]
The merged list will be 
[1, 2, 3, 4, 5, 6, 7, 8, 9].


An efficient solution is to use heap data structure. The time complexity of heap based solution is O(N Log k).

1. Create an output array.
2. Create a min heap of size k and insert 1st element in all the arrays into the heap
3. Repeat following steps while priority queue is not empty.
…..a) Remove minimum element from heap (minimum is always at root) and store it in output array.
…..b) Insert next element from the array from which the element is extracted. If the array doesn’t have any more elements, then do nothing.
"""
from heapq import heappush,heappop
def merge(numbers):
    # code here
    # return merged list
    ans = []
    heap = []
    n = len(numbers)
    for i in range(n):
        heappush(heap,[numbers[i][0],i,0])

    while heap:
        curr,r,c = heappop(heap)
        ans.append(curr)

        if c < n - 1:

            heappush(heap,[numbers[r][c+1],r,c+1])
    return ans
"""
TC = o(n log n)
SC = o(n)
"""