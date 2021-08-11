"""
In Doraland, people have unique Identity Numbers called D-id.
Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K
gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop
and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number
of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.

Example 1:

Input:
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
Output: 
1 2
Explanation: 
Customers with D-id 1 and 2 are most 
frequent.
"""
from heapq import heappush,heappop
class Solution:
    def TopK(self, array, k):
        # code here
        dic = {}
        for i in array:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        heap = []
        for i in dic:
            heappush(heap,[dic[i],i])
            if len(heap) > k:
                tmp = heappop(heap)
                if len(heap) > 0:
                    tmp2 = heap[0]
                    if tmp[0] == tmp2[0]:
                        if tmp[1] > tmp2[1]:
                            heappop(heap)
                            heappush(heap,tmp)
        ans = []
        while heap:
            ans.append(heappop(heap)[1])
        ans.reverse()
        return ans
