def maxAmount(arr, n):
	   	dp = [[0 for i in range(n)]for i in range(n)]
	   	for i in range(n):
	   	    for j in range(i,n):
	   	        gap = j - i 
	   	        x = 0
	   	        if gap+2 <= j:
	   	            x = dp[gap+2][j]
	   	        y = 0
	   	        if gap+1 <= j - 1:
	   	            y = dp[gap+1][j-1]
	   	        z = 0
	   	        if gap <= j - 2:
	   	            z = dp[gap][j-2]
	   	        dp[gap][j] = max((arr[gap] + min(x,y)),arr[j] + min(y,z))
	   	return dp[0][n-1]