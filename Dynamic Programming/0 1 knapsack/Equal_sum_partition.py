def equalPartition(N, arr):
    # code here
    if sum(arr)%2 != 0:
        return 0
    else:
        target = sum(arr)//2
        dp = [[False for i in range(target+1)]for i in range(N+1)]
        for i in range(N+1):
            for j in range(target+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                elif arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return int(dp[N][target])