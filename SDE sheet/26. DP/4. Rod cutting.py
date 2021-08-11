"""
Same as Unbounded Knapsack with a different Problem statement
"""
def rod_cutting(arr,n):
    wt = [i for i in range(1,n+1)]
    dp = [[0 for i in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if wt[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i][j-wt[i-1]]+arr[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][n]
print(rod_cutting([1,5,8,9,10,17,17,20],8))





