def substring(a,b,n,m):
    dp = [[0 for i in range(m+1)]for i in range(n+1)]
    ans = float('-inf')
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                if dp[i][j] > ans:
                    ans = dp[i][j]
            else:
                dp[i][j] = 0
    if ans == float('inf'):
        return -1
    return ans
print(substring("abcd","bc",4,2))