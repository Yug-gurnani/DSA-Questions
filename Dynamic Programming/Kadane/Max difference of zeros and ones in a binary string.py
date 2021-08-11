def maxSubstring(S):
		# code here
    if all(i == "1" for i in S):
        return -1
    arr = list(S)
    for i in range(len(S)):
        if arr[i] == "0":
            arr[i] = 1
        else:
            arr[i] = -1
    lsum = arr[0]
    gsum = arr[0]
    for i in range(1,len(arr)):
        lsum = max(arr[i],lsum+arr[i])
        if lsum > gsum:
            gsum = lsum
    return gsum