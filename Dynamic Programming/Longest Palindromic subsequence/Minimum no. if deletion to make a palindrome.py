def deletions(s):
    s1 = s[::-1]
    n = len(s)
    dp = [[0 for i in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s1[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return n-dp[n][n]