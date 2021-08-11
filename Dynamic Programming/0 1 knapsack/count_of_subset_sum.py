for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    s = int(input())
    dp = [[0 for i in range(s+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j == 0:
                dp[i][j] = 1
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][s])