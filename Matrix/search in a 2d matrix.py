"""
o(n+m)
"""
def searchMatrix(arr, t):
    if arr == [] or arr == [[]]:
        return False
    else:
        m = len(arr)
        n = len(arr[0])
        s = 0
        e = n-1
        
        while s < m and e >= 0:
            if t > arr[s][e]:
                s += 1
            elif t < arr[s][e]:
                e -= 1
            elif t == arr[s][e]:
                return True
        return False