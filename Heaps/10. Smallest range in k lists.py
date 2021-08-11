from heapq import heapify,heappush,heappop
def smallestRange(numbers):
    k = len(numbers)
    n = len(numbers[0])
    curmin = numbers[0][0]
    curmax = numbers[0][0]
    #Init heap with size k heap element format = (int,(row,col))
    heap = []
    for i in range(k):
        if numbers[i][0] < curmin:
            curmin = numbers[i][0]
        if numbers[i][0] > curmax:
            curmax = numbers[i][0]
        
        heappush(heap,(numbers[i][0],(i,0)))
    
    minele = curmin 
    maxele = curmax
    
    while(heap[0][1][1] < n-1):
        ele = heappop(heap)
        newele = numbers[ele[1][0]][ele[1][1]+1]
        
        curmax = max(newele,curmax)
        heappush(heap,(newele,(ele[1][0],ele[1][1] + 1)))
        curmin = heap[0][0]
        if (curmax - curmin) < (maxele - minele):
            maxele = curmax
            minele = curmin
    return (minele,maxele)
        