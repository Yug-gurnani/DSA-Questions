arr = [10,3,40,20,50,80,70]
ele = 80
low = 0
high = len(arr)-1
while low <= high:
    mid = low +(high-low)//2
    if arr[mid] == ele:
        print(mid)
    if mid - 1 >= low and arr[mid-1] == ele:
        print(mid-1)
    if mid + 1 <= high and arr[mid+1] == ele:
        print(mid + 1)
    else:
        if arr[mid] > ele:
            high = mid - 2
        else:
            low = mid + 2
