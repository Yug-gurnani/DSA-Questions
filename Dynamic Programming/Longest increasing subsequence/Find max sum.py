def FindMaxSum(arr, n):
    dp = [0 for x in range(n)]
    if n == 1:
        return arr[0]
    dp[0] = arr[0]
    dp[1] = max(arr[1],arr[0])
    for i in range(2,n):
        dp[i] = max(dp[i-2]+arr[i],dp[i-1])
    return dp[n-1]