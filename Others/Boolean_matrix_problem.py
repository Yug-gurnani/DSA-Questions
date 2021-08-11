for _ in range(int(input())):
    m,n = map(int,input().split())
    arr = []
    for i in range(m):
        temp = list(map(int,input().split()))
        arr.append(temp)
    row = [0]*m
    col = [0]*n
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                row[i] = 1
                col[j] = 1
    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                arr[i][j] = 1
    for i in range(m):
        for j in range(n):
            print(arr[i][j],end = " ")
        print()
        