arr = [9,8,7,6,5,4,3,2,1]
ele = 3
low = 0
high = len(arr)-1
while low <= high:
    mid = low + (high - low)//2
    if arr[mid] == ele:
        print(mid)
        break
    elif arr[mid] > ele:
        low = mid+1
    else:
        high = mid-1
