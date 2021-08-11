"""
Given an input stream of N integers.
The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

Example 1:

Input:
N = 4
X[] = 5,15,1,3
Output:
5
10
5
4
Explanation:Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5) 
15 goes to stream --> median 10 (5,15) 
1 goes to stream --> median 5 (5,15,1) 
3 goes to stream --> median 4 (5,15,1 3)

Idea is to use two priority_queue one acting as min heap and other acting as max heap
Firstly median of an array is its central element if size is odd else sum of middle elements
in case of even elemnts.
So we will store all the numbers lesser than a number in Max heap and all number greater
than a number in Min heap
eg 1>. 5 6 7 8 9
:We start from 5 we put it in Max Heap and median=5
:Then comes 6 since 6 is greater than 5 we put it in Min Heap median=(5+6)/2
:Then comes 7 since it is greater than 5 we put it too in Min heap but size of min heap 
should be one less than or equal to max heap. so we shift 6 from min to max heap.
now max heap = 6 5 min heap = 7 median=6 
:Then comes 8 since 8>6 we put in Min heap. median=(6+7)/2
:Then comes 9 since 9>6 we put it in Min heap but min_heap.size>max_heap.size so we shift
7 from min heap to max heap. Now min_heap= 7 6 5 max_heap =8 9 median=7
"""
from heapq import heappush,heappop
def balanceHeaps():
    global min_heap,max_heap
    if len(max_heap) - len(min_heap) == 2:
        tmp = heappop(max_heap)
        heappush(min_heap,-1*tmp)
    else:
        if len(min_heap) - len(max_heap) == 1:
            tmp = heappop(min_heap)
            heappush(max_heap,-1 * tmp)
    
def getMedian():
    global min_heap,max_heap
    #print(max_heap,min_heap)
    if len(max_heap) == len(min_heap):
        return int((-1 * max_heap[0] + min_heap[0])/2)
    else:
        return -1 * max_heap[0]
    
def insertHeaps(x):
    global min_heap,max_heap
    if not max_heap:
        heappush(max_heap,-1 * x)
    else:
        if x > -1*max_heap[0]:
            heappush(min_heap,x)
            balanceHeaps()
        else:
            heappush(max_heap,-1 * x)
            balanceHeaps()
"""
TC = o(n log n)
SC = o(n)
"""