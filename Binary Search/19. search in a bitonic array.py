def bn(arr,low,high,ele):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high = mid - 1
        else:
            low = mid + 1
    return -1
def bnrev(arr,low,high,ele):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            high = mid - 1
        else:
            low = mid + 1
    return -1
            
arr = [3, 8, 9, 20, 17, 5, 1]

ele = 8

def peakElement(arr, n):
    if n == 1:
        return 0
    low = 0
    high = n-1
    while low <= high:
        mid = low + (high - low)//2
        if mid == 0 and arr[mid] > arr[mid+1]:
            return mid
        elif mid == n-1 and arr[mid] > arr[mid - 1]:
            return mid
        elif arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        else:
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
    return mid
peak = peakElement(arr,len(arr))

if ele == arr[peak]:
    print(peak)
a = (bn(arr,0,peak,ele))
b = (bnrev(arr,peak,len(arr)-1,ele))
print(max(a,b))