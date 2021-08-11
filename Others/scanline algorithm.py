n,p = map(int,input().split())
arr = [0 for i in range(p+2)]
for i in range(n):
    a,b = map(int,input().split())
    if a-b < 0:
        l1 = 0
    else:
        l1 = a-b
    if a +b > p:
        r1 = p
    else:
        r1 = a+b
    arr[l1] += 1
    arr[r1+1] -=1
#print(arr)
for i in range(1,p+1):
    arr[i] = arr[i-1]+arr[i]
ans = 0
cnt = 0
#print(arr)
for i in range(p+1):
    if arr[i]!= 1:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
ans = max(ans,cnt)
print(ans)