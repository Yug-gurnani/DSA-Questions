for _ in range(int(input())):
    n = int(input())
    vals = list(map(int,input().split()))
    s = int(input())
    dp = [[False for i in range(s+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif j >= vals[i-1]:
                dp[i][j] = dp[i-1][j-vals[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][s])