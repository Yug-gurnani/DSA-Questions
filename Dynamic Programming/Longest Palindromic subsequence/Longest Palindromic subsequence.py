def lps(s1,n):
    dp = [[0 for i in range(n+1)]for i in range(n+1)]
    s2 = s1[::-1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]
print(lps("agbcba",6))