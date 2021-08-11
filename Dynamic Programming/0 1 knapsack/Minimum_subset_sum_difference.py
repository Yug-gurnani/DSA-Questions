def minimum_diff(arr,n):
    range_ = sum(arr)
    dp = [[False for i in range(range_+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(range_ + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1],range_
arr,r = minimum_diff([1,6,11,5],4)
mn = float("inf")
for i in range(len(arr)):
    if i*2 > r:
        break
    elif arr[i] and r-i*2 < mn:
        mn = r-i*2
print(mn)