"""

Given an input stream arr[] of n integers, find the kth largest element for each element in the stream.

Example 1:

Input:
k = 4, n = 6
arr[] = {1, 2, 3, 4, 5, 6}
Output:
-1 -1 -1 1 2 3
Explanation:
k = 4
For 1, the 4th largest element doesn't
exist so we print -1.
For 2, the 4th largest element doesn't
exist so we print -1.
For 3, the 4th largest element doesn't
exist so we print -1.
For 4, the 4th largest element is 1.
For 5, the 4th largest element is 2.
for 6, the 4th largest element is 3.
"""
from heapq import heappush,heappop
class Solution:
    def kthLargest(self, k, arr, n):
        # code here
        ans = []
        heap = []
        for i in range(n):
            heappush(heap,arr[i])
            if len(heap) == k:
                ans.append(str(heappop(heap)))
                
            else:
                ans.append(str(-1))
        return ans
"""
TC = o(n log k)
SC = o(k)
"""