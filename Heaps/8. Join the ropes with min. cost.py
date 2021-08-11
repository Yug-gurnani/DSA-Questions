min_heap = []
arr = [1,2,3,4,5]
from heapq import heappush,heappop,heapify
cost = 0
min_heap = arr[:]
heapify(min_heap)
for i in arr:
    if len(min_heap) >= 2:
        a = heappop(min_heap)
        b = heappop(min_heap)
        heappush(min_heap,a+b)
        cost += a+b
print(cost)
