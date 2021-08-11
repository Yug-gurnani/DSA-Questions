def solve(e,f,dp):
    if e == 1 or f == 0 or f == 1:
        dp[f][e] = f
        return dp[f][e]
    if dp[f][e] != -1:
        return dp[f][e]
    mn = float('inf')
    for k in range(1,f):
        temp = 1+max(solve(e-1,k-1,dp),solve(e,f-k,dp))
        '''
        1st condition is when we have to check all bottom floors and we have now e-1 eggs left and k-1 floors left
        2nd condition the egg doesnt break and we have to all eggs remaining and we have to check all upper floors i.e. f-k floors
        '''
        mn = min(mn,temp)
    dp[f][e] = mn
    return dp[f][e]
dp = [[-1 for i in range(3)]for i in range(5)] 
print(solve(2,4,dp))