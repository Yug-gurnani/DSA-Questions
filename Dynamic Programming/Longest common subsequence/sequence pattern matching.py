def spm(a,b,n,m):
    dp = [[0 for i in range(n+1)]for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if b[i-1] == a[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    if dp[m][n] == len(a):
        return True 
    return False
print(spm("AXYZ","ADXCPY",4,6))