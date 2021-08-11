def findKRotation(arr,  n):
        # code here
    if n == 1:
        return 0
    if arr[0] < arr[n-1]:
        return 0
    low = 0
    high = n-1
    if arr[low] <= arr[high]:
        return low    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        mid = low + (high-low)//2
        prev = (mid + n - 1)%n
        nex = (mid + 1)%n 
        if arr[mid] <= arr[prev] and arr[mid] <= arr[nex]:
            return mid
        elif arr[mid] >= arr[low]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
