def sumSubstrings(s):
    n = len(s)
    mod = 1000000007
    dp = [0 for i in range(n)]
    dp[0] = int(s[0])
    for i in range(1,n):
        dp[i] = (i+1)*int(s[i]) + (10*dp[i-1])
    return sum(dp)%mod