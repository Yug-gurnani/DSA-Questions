def lrs(s,n):
    a = s
    dp = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                continue
            elif s[i-1] == a[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp[n-1][n-1])