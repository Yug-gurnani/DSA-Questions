def LongestBitonicSequence(arr):
    n = len(arr)
    inc = [1 for i in range(n)]
    dec = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i],inc[j]+1)
    for i in range(n-2,-1,-1):
        for j in range(n-1,i,-1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i],dec[j] + 1)
    #print(inc,dec)
    ans = [None for i in range(n)]
    for i in range(n):
        ans[i] = inc[i] + dec[i] - 1
    return max(ans)