def search(arr):
    start = 0
    end = 1
    while arr[end] == 0:
        start = end
        end *= 2
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == 1:
            if mid == 0:
                return mid
            else:
                res = mid
                end = mid - 1
        elif arr[mid] == 0:
            start = mid + 1
    return res
