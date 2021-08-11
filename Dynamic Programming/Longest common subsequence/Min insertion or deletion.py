def minOperations(s1, s2):
		# code here
		a = len(s1)
		b = len(s2)
		dp = [[0 for i in range(b+1)]for i in range(a+1)]
		for i in range(1,a+1):
		    for j in range(1,b+1):
		        if s1[i-1] == s2[j-1]:
		            dp[i][j] = 1+dp[i-1][j-1]
		        else:
		            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		return a+b-(2*dp[a][b])
print(minOperations("heap","pea"))
"""
for no. of deletions :- len(s1) - lcs
for no. of insertions :- len(s2) - lcs
"""