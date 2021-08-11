for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if k == 1:
        lsum = arr[0]
        gsum = arr[0]
        for i in range(1,n):
            lsum = max(arr[i],lsum+arr[i])
            gsum = max(gsum,lsum)
        print(gsum)
    elif k == 2:
        pass
        