def find(arr,ele):
    low = 0
    high = len(arr)-1
    ans = len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == ele:
            print(mid)
            break
        elif arr[mid] >= ele:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
"""
for stopping overflow
use mid = start + (end - start)//2
"""