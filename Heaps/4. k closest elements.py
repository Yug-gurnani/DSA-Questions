from heapq import heappush,heappop
arr = [7,1,5,9,6,8]
k = 3
n = 7
max_heap = []
for i in range(len(arr)):
    heappush(max_heap,[abs(arr[i]-n)*-1,arr[i]])
    if len(max_heap) > k:
        heappop(max_heap)
while max_heap:
    print(heappop(max_heap)[1],end = " ")
    