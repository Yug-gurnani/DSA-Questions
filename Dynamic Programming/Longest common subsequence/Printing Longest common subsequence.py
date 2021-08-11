def lcs(x,y,a,b):
    dp = [[0 for i in range(a+1)]for i in range(b+1)]
    for i in range(1,b+1):
        for j in range(1,a+1):
            if y[i-1] == x[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp
dp = lcs("abcdefg","aefgr",7,5)
def printing(dp,x,y):
    ans = ""
    a = len(y)
    b = len(x)
    while a > 0 or b > 0:
        if x[b-1] == y[a-1]:
            ans += x[b-1]
            a -= 1
            b -= 1
        else:
            if dp[a-1][b] > dp[a][b-1]:
                a -= 1
            else:
                b -= 1
    return ans[::-1]
    
print(printing(dp,"abcdefg","aefgr"))