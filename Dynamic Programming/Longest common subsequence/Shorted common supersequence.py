def scs(n,m):
    a = len(n)
    b = len(m)
    dp = [[0 for i in range(b+1)]for i in range(a+1)]
    for i in range(1,a+1):
        for j in range(1,b+1):
            if n[i-1] == m[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return a+b-dp[a][b]
print(scs("geek","eke"))