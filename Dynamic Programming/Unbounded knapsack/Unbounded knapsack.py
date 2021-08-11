def unbounded_knapsack(vals,wt,n,w):
    dp = [[0 for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i][j-wt[i-1]]+vals[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]
print(unbounded_knapsack([1,4,5,7],[1,3,4,5],4,8))