arr = [1,2,5,7,9,10,13,14]
ele = 7
if ele < arr[0]:
    print(0)
elif ele > arr[-1]:
    print(-1)
else:
    low = 0
    high = len(arr) - 1
    res = None
    while low <= high:
        mid = low + (high - low) //2
        if arr[mid] > ele:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
print(res)