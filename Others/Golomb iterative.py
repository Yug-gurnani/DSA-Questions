def kadane(arr):
    lsum = arr[0]
    gsum = arr[0]
    for i in range(1,len(arr)):
        lsum = max(arr[i],lsum+arr[i])
        gsum = max(lsum,gsum)
    return gsum
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    m = int(input())
    brr = list(map(int,input().split()))
    print(max(0,arr[0],brr[0],kadane(arr)+kadane(brr)))

