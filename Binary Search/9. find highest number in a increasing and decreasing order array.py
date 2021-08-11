def findPeakElement(arr):
    n = len(arr)
    low = 0
    high = n-1
    if n == 2:
        return max(arr[0],arr[1])
    while low <= high:
        if arr[low] < arr[high]:
            return arr[high]
        mid = low + (high-low)//2
        prev = (mid + n - 1)%n
        nex  = (mid+1)%n
        if arr[mid] > arr[prev] and arr[mid] > arr[nex]:
            return arr[mid]
        elif arr[mid] > arr[low]:
            low = mid + 1
        else:
            high = mid - 1