for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    dic = dict()
    s = 0
    ans = 0
    for i in range(n):
        s += arr[i]
        if s == k:
            ans = i + 1
        if s-k in dic:
            ans = max(ans,i - dic[s-k])
        if s not in dic:
            dic[s] = i
    print(ans)