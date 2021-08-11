arr = [1,2,3,5,5,5,7,8,9]
ele = 5
low = 0
first,second = None,None
high = len(arr)-1
while low <= high:
    mid = low + (high - low)//2
    if arr[mid] == ele:
        if mid == 0:
            first = 0
            break
        else:
            first = mid
            high = mid - 1
    elif arr[mid] > ele:
        high = mid -1
    else:
        low = mid + 1
low = 0
high = len(arr)-1
while low <= high:
    mid = low + (high - low)//2
    if arr[mid] == ele:
        if mid == len(arr)-1:
            second = len(arr)-1
            break
        else:
            second = mid
            low = mid +1
    elif arr[mid] > ele:
        high = mid -1
    else:
        low = mid + 1
print(first,second)
 