for _ in range(int(input())):
    m,n = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    prod = [0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            prod[i+j] += a[i]*b[j]
    print(*prod)