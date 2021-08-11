from heapq import heappush,heappop
def findkth(arr,k):
    max_heap = []
    for i in arr:
        heappush(max_heap,-1*i)
        if len(max_heap) > k:
            heappop(max_heap)
    return max_heap[0]*-1
k1 = 3
k2 = 6
arr = [1,15,11,3,12,4]
s = 0
for i in arr:
    if i > findkth(arr,k1) and i < findkth(arr,k2):
        s += i
print(s)