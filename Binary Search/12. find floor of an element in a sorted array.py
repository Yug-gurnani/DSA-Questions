def findFloor(arr,n,x):
    if x < arr[0]:
        return -1
    if x > arr[n-1]:
        return n-1
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x and mid+1 <= high and arr[mid + 1] > x:
            return mid
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1