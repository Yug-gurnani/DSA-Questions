def minDeletions(arr, n):
		# code here
		dp = [1 for i in range(n+1)]
		for i in range(1,n):
		    for j in range(i):
		        if arr[i] > arr[j]:
		            dp[i] = max(dp[i],dp[j]+1)
		#print(dp)
		return n - max(dp)