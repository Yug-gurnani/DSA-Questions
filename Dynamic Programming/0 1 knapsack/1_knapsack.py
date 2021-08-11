for _ in range(int(input())):
    n = int(input())
    w = int(input())
    vals = list(map(int,input().split()))
    weights = list(map(int,input().split()))
    dp = [[-1 for i in range(w+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i-1] <= j:
                dp[i][j] = max(vals[i-1] + dp[i-1][j-weights[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    print(dp[n][w])