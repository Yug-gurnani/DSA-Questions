
import heapq
max_heap = []
arr = [3,7,10,4,15,20]
k = 3
for i in range(len(arr)):
    heapq.heappush(max_heap,-1 * arr[i])#because by default it is min heap thats why we multiply it by -1
    #print(max_heap)
    if len(max_heap) > k:
        heapq.heappop(max_heap)
print(max_heap[0]*-1)