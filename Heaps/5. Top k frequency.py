arr = [1,1,1,4,3,3,2,2]
k = 3
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
min_heap = []
from heapq import heappush,heappop
for i in dic:
    heappush(min_heap,[dic[i],i])
    if len(min_heap) > k:
        heappop(min_heap)
print(min_heap)
