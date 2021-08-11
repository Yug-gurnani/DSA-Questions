def util(x,y,n):
    dp = [[0 for x in range(n+1)]for x in range(n+1)]
    for i in range(n+1):
        print(dp)
        for j in range(n+1):
            print(dp)
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[n][n]
for _ in range(int(input())):
    s = input()
    n = len(s)
    x = s[:]
    y = x[::-1]
    print(util(x,y,n))

    


    
    