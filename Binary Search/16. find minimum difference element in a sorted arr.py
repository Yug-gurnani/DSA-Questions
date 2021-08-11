def search(arr,key):
    low = 0
    high = len(arr)-1
    floor = float('inf')
    ceil = float('inf')
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
            floor = arr[mid]
    return min(abs(floor - key),abs(ceil - key))
print(search([2,4,9,11],1))