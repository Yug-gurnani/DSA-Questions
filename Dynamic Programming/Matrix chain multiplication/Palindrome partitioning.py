def solve(s,i,j,mn,dp):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i:j+1] == s[i:j+1][::-1]:
        return 0
    for k in range(i,j):
        temp = solve(s,i,k,mn,dp)+solve(s,k+1,j,mn,dp) +1
        if temp < mn:
            mn = temp
    dp[i][j] = mn
    return dp[i][j]
    
dp = [[-1 for i in range(500)]for i in range(500)]
mn = float('inf')
print(solve("leet",0,3,mn,dp))