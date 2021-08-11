def solve(arr,n,k):
    i = 0
    currsum = 0
    ans = 0
    j = 0
    while i <= n -k+1 and j < n:
        currsum += arr[j]
        if j - i + 1 < k:
            j += 1
        else:
            ans = max(currsum,ans)
            currsum -= arr[i]
            i += 1
            j += 1
    print(ans)
solve([1,2,3,4,5],5,4)
        
        
        