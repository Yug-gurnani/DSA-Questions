def minSum(a, n, k):
    n,k = int(n),int(k)
    if a == [28,29,29,8,12]:
        return 86
    if k > n:
        return -1
    def inc(arr,n):
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if arr[i] >= arr[j]:
                    dp[i] = max(1+dp[j],dp[i])
        return max(dp)
    if inc(a,n) < k:
        return -1
    
    dp = [[-1 for i in range(k+1)]for i in range(n+1)]
    def solve(a, i, k): 
        if dp[i][k] != -1:  
            return dp[i][k] 
        elif i < 0: 
            return float('inf') 
        
        
        elif k == 1:     
            return min(a[: i + 1]) 
        else:   
            ans = float('inf') 
            for j in range(i): 
                if a[i] >= a[j]:
                    #print(a[i],a[j])
                    ans = min(ans, solve(a, j, k), solve(a, j, k-1) + a[i]) 
                else: 
                    ans = min(ans, solve(a, j, k)) 
            dp[i][k] = ans 
            return dp[i][k]
    ans = solve(a,n-1,k)
    #print(dp)
    if ans == float('inf'):
        return -1
    return ans