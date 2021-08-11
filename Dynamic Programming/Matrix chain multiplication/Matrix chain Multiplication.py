def solve(arr,i,j,mn,dp):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    for k in range(i,j):
        dp[i][j] = solve(arr,i,k,mn,dp)+solve(arr,k+1,j,mn,dp)+(arr[i-1]*arr[k] * arr[j])
        if dp[i][j] < mn:
            mn = dp[i][j]
    return mn
mn = float('inf')
dp = [[-1 for i in range(1001)]for i in range(1001)]
print(solve([10,20,30,40,30],1,4,mn,dp))
