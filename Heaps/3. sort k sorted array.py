import heapq
min_heap = []
arr = [2,6,3,12,56,8]
k = 3
for i in arr:
    heapq.heappush(min_heap,i)
    if len(min_heap) > k:
        print(heapq.heappop(min_heap))
while len(min_heap) > 0:
    print(heapq.heappop(min_heap))
    