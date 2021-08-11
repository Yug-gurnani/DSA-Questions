from heapq import heappush,heappop
dic = {}
arr = [1,1,1,4,2,2,3,3,5]
res = []
min_heap = []
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic:
    heappush(min_heap,[-1*dic[i],i])
#print(min_heap)
while min_heap:
    temp = heappop(min_heap)
    res.extend([temp[1]]*(-1*temp[0]))
print(res)