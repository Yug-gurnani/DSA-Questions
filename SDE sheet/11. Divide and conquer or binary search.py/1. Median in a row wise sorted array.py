"""
Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

Example 1:

Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5

Explanation:
Sorting matrix elements gives us 
{1,2,3,3,5,6,6,9,9}. Hence, 5 is median.

we first get the min. and max. element from the matrix and then apply binary search on it and find the median
"""
def median(self, matrix, r, c):
    def upperbound(arr,m):
        low = 0
        high = len(arr)-1
        res = 0
        while low <= high:
            mid = (low + high)//2
            if arr[mid] > m:
                res = mid
                high = mid - 1
            else:
                low = mid +1
        return low
    #code here
    k = ((r*c)+1)//2
    a = float('inf')
    b = -1
    for i in range(r):
        a = min(matrix[i][0],a)
        b = max(matrix[i][-1],b)
    
    while a < b:
        mid = (a+b)//2
        cnt = 0
        for i in range(r):
            #print(upperbound(matrix[i],mid),mid)
            cnt = cnt + upperbound(matrix[i],mid)
        if cnt < k:
            a = mid + 1
        else:
            b = mid
    return a
"""
TC = o(r * log(c))
SC = o(1)
"""