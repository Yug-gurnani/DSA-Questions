def count_of_subset(arr,n,diff):
    s1 = (sum(arr)+diff)//2
    dp = [[0 for i in range(s1+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(s1+1):
            if j == 0:
                dp[i][j] = 1
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][s1])
count_of_subset([1,1,2,3],4,3)