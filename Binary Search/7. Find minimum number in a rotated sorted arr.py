def minNumber(arr,low,high):
    n = len(arr)
    if arr[low] <= arr[high]:
        return arr[low]
    while low <= high:
        if arr[low] <= arr[high]:
            return arr[low]
        mid = low + (high-low)//2
        prev = (mid + n - 1)%n
        nex = (mid + 1)%n 
        if arr[mid] <= arr[prev] and arr[mid] <= arr[nex]:
            return arr[mid]
        elif arr[mid] >= arr[low]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
    return arr[mid]