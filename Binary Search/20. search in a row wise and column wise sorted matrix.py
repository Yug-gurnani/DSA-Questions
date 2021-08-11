def matSearch(arr, n, m, x):
    low = 0
    high = m-1
    while low <= n-1 and high >= 0:
        if arr[low][high] == x:
            return 1
        elif arr[low][high] > x:
            high -= 1
        else:
            low += 1
            
    return 0