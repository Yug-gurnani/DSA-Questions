"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""
def merge(self,arr: List[List[int]]) -> List[List[int]]:
    i = 0
    n = len(arr)
    arr.sort() #in case arr is not sorted
    while i < n-1:
        if arr[i][1] >= arr[i+1][0]:
            arr[i][1] = max(arr[i][1],arr[i+1][1])
            del arr[i+1]
            i -= 1
            n = len(arr)
        i += 1
    return arr
"""
TC = O(n) or  o(n log n) in case of unsorted array
SC = O(1)
"""