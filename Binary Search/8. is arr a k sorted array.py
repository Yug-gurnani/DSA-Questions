def isKSortedArray(arr, n, k): 
        def binarysearch(arr,n,ele):
            low = 0
            high = n-1
            while low <= high:
                mid = low + (high - low)//2
                if ele == arr[mid]:
                    return mid
                elif arr[mid] > ele:
                    high = mid - 1
                else:
                    low = mid + 1
        brr = arr.copy()
        brr.sort()
    
        for i in range(len(arr)):
            j = binarysearch(brr,n,arr[i])
            if abs(i-j) > k:
                return "No"
        return "Yes"