def solve(arr,n,k):
    i = 0
    j = 0
    ans = 0
    s = 0
    while j < n:
        s += arr[j]
        if s < k:
            j += 1
        elif s == k:
            ans = max(ans,j-i+1)
            j += 1
        elif s > k:
            while s > k:
                s -= arr[i]
                i += 1
            j += 1
    return ans
print(solve([4,1,1,1,2,3,5],7,5))