"""
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.

we have used max_heap for this to reduce time complexity
"""
def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    from heapq import heappush,heappop
    heap = []
    for i in range(n):
        heappush(heap,-1*arr[i])
        if len(heap) > k:
            heappop(heap)
    return -1 * heappop(heap)
"""
TC = o(n log k)
SC = o(k)
"""