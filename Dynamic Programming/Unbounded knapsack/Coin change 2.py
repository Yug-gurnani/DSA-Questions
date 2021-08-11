def coin_change2(arr,n,s):
    dp = [[0 for i in range(s+1)]for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(s+1):
        dp[0][i] = float('inf')-1
    for i in range(1,s+1):
        if i%arr[0] == 0:
            dp[1][i] = i//arr[0]
        else:
            dp[1][i] = float('inf')-1
    for i in range(2,n+1):
        for j in range(1,s+1):
            if arr[i-1] <= j:
                dp[i][j] = min(dp[i-1][j],1+dp[i][j-arr[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    if dp[n][s] == float('inf')-1:
        return -1
    return dp[n][s]
print(coin_change2([25,10,5],3,30))