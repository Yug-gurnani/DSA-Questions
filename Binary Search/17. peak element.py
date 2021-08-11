def peakElement(arr, n):
    if n == 1:
        return 0
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high - low)//2
        if mid == 0 and arr[mid] > arr[mid+1]:
            return mid
        elif mid == n-1 and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        else:
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
    return mid