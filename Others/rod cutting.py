dp = [0]*5005
dp[0] = 0
n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)

for i in range(1,n+1):
	dp[i] = 0
	for l in range(1,i+1):
		dp[l] = arr[l]+dp[i-l]
print(dp[n])

