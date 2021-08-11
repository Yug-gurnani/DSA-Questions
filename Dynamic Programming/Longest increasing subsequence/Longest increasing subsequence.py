arr = [5,4,3,2,1]
n = len(arr)
dp = [1 for i in range(n)]
for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))