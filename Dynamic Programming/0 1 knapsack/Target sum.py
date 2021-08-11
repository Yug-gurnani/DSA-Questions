def targetsum(nums,S):
    n = len(nums)
    target = (sum(nums)+S)//2
    dp = [[0 for i in range(target+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = 1
            elif nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
    return dp[n][target]
print(targetsum([1,1,1,1,1],3))