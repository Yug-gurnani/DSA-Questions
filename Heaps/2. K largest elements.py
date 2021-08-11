import heapq
min_heap = []
arr = [10,4,20,7,15,3]
k = 3
for i in arr:
    heapq.heappush(min_heap,i)
    if len(min_heap) > k:
        heapq.heappop(min_heap)
print(min_heap)