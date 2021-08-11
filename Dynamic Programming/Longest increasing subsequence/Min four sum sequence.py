def minSum(arr, n):
    # Code here
    dp = [0] * n
    if n <= 4:
        return min(arr)
    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[2]
    dp[3] = arr[3]
    for i in range(4,n):
        dp[i] = arr[i] + min(dp[i-1],dp[i-2],dp[i-3],dp[i-4])
    return min(dp[n-1],dp[n-2],dp[n-3],dp[n-4])
    