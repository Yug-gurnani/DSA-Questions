def search(arr,key):
    start = 0
    end = 1
    while arr[end] < key:
        start = end
        end *= 2
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == key:
            print(mid)
            break
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
