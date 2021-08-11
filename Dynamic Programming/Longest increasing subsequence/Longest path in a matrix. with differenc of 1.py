def lpm(i,j,arr,dp,n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    w,x,y,z = -1,-1,-1,-1
    if i > 0 and (arr[i][j] + 1 == arr[i-1][j]):
        w = 1 + lpm(i-1,j,arr,dp,n)
    if i < n - 1 and (arr[i][j]+1 == arr[i+1][j]):
        x = 1 + lpm(i+1,j,arr,dp,n)
    if j > 0 and (arr[i][j] + 1 == arr[i][j-1]):
        y = 1 + lpm(i,j-1,arr,dp,n)
    if j < n - 1 and (arr[i][j]+1 == arr[i][j+1]):
        z = 1 + lpm(i,j+1,arr,dp,n)
    dp[i][j] = max(w,x,y,z,1)
    return dp[i][j]
for _ in range(int(input())):
    n = int(input())
    brr = list(map(int,input().split()))
    temp = []
    arr = []
    for i in range(n*n):
        if len(temp) == n:
            arr.append(temp)
            temp = []
        temp.append(brr[i])
    arr.append(temp)
    res = 0
    dp = [[-1 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                lpm(i,j,arr,dp,n)
            res = max(dp[i][j],res)
    print(res)  