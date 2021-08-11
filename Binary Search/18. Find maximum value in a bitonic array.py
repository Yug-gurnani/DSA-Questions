arr = [1,4,8,12,3,2]
low = 0
high = len(arr)-1
while low <= high:
    mid = low + (high - low)//2
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        print(mid)
        break
    elif arr[mid] > arr[mid + 1]:
        high = mid - 1
    else:
        low = mid + 1