def countWays(self, S1, S2):
        # code here
    dp = [[0 for i in range(len(S2)+1)]for i in range(len(S1)+1)]
    for i in range(len(S1)+1):
        for j in range(len(S2)+1):
            if j == 0:
                dp[i][j] = 1
            elif S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(S1)][len(S2)]