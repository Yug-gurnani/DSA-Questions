"""
Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. Help her find out K's closest neighbors.
Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.

Example 1:

Input:
N = 4, X = 0, K = 4
a[] = {-21, 21, 4, -12, 20}, 
Output:
-21 -12 4 20
Explanation:
The closest neighbour is house
number 4. Followed by -12 and 20. -21 and 21 
are both equal distance from X=0. Therefore, 
Lucy can only pick 1. Based on the given 
condition she picks -21 as it is the smaller 
of the two. 
"""
from heapq import heappush,heappop
class Solution:
    def Kclosest(self, arr, n, x, k):
        # Your code goes here
        heap = []
        for i in range(n):
            heappush(heap,[-1 * abs(x - arr[i]),arr[i]])
            if len(heap) > k:
                tmp = heappop(heap)
                tmp2 = heap[0]
                if tmp[0] == tmp2[0]:
                    if tmp[1] < tmp2[1]:
                        heappop(heap)
                        heappush(heap,tmp)
                else:
                    pass
        ans = []
        for i in heap:
            ans.append(i[1])
        return sorted(ans)
"""
TC = o(o n log n)
SC = o(n)
"""