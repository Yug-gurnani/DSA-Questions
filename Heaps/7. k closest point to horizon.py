from heapq import heappush,heappop
max_heap = []
arr = [[1,0],[2,1],[3,6],[-5,2],[1,-4]]
k = 3
for i in arr:
    heappush(max_heap,[(i[0]**2+i[1]**2)*-1,i])
    if len(max_heap) > 3:
        heappop(max_heap)
print(max_heap)