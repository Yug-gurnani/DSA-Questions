def is_scramble(S1,S2,dp):
    if len(S1) != len(S2):
        return False
    n = len(S1)
    if n == 0:
        return True
    if dp[n][n] != None:
        return dp[n][n]
    if S1 == S2:
        return True
    if sorted(S1) != sorted(S2):
        return False
    
    for i in range(1,n):
        if is_scramble(S1[:i],S2[:i],dp) and is_scramble(S1[i:],S2[i:],dp):
            dp[n][n] = True
            return dp[n][n]
        else:
            dp[n][n] = False
        #-i cause of checking reverse string condition
        if is_scramble(S1[-i:],S2[:i],dp) and is_scramble(S1[:-i],S2[i:],dp):
            dp[n][n] = True
            return dp[n][n]
        else:
            dp[n][n] = False
    return False
a ="rskuqzchcsc"
b = "shccucrkqzs"
dp = [[None for i in range(len(a)+1)]for i in range(len(b)+1)]
print(is_scramble(a,b,dp))
