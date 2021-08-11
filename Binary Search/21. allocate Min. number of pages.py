"""
Very Important problem 
same problems:
Painter partition
Divide choclate
Pig race
Aggresive cow
"""
def findPages(arr, n, m):
    def isvalid(arr,n,m,mx):
        s = 0
        stu = 1
        for i in range(n):
            s += arr[i]
            if s > mx:
                stu += 1
                s = arr[i]
            if stu > m:
                return False
        if stu <= m:
            return True
        return False
    def binary(arr,low,high):
        res = -1
        while low <= high:
            mid = low + (high - low)//2
            if isvalid(arr,n,m,mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
    if m > n:
        return -1
    return binary(arr,max(arr),sum(arr))
