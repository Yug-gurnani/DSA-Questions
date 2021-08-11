def coin_change(coins,n,s):
    dp = [[0 for i in range(s+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(s+1):
            if j == 0:
                dp[i][j] = 1
            elif coins[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][s]
print(coin_change([2,3,5],3,9))