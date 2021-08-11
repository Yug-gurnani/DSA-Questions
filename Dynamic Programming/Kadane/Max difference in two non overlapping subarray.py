def leftmax(arr,n,left):
    lmax = arr[0]
    gmax = arr[0]
    left[0] = arr[0]
    for i in range(1,n):
        lmax = max(arr[i],lmax + arr[i])
        gmax = max(lmax,gmax)
        left[i] = gmax
    return gmax
def rightmax(arr,n,right):
    lmax = arr[n-1]
    gmax = arr[n-1]
    right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        lmax = max(arr[i],lmax + arr[i])
        gmax = max(lmax,gmax)
        right[i] = gmax
    return gmax
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    leftmin = [0 for i in range(n)]
    rightmin = [0 for i in range(n)]
    invertarr = [0 for i in range(n)]
    for i in range(n):
        invertarr[i] = -arr[i]
    leftmax(arr,n,left)
    rightmax(arr,n,right)
    leftmax(invertarr,n,leftmin)
    rightmax(invertarr,n,rightmin)
    for i in range(n):
        leftmin[i] = -leftmin[i]
        rightmin[i] = -rightmin[i]
    result = -2147483648
    for i in range(n-1):
        absvalue = max(abs(leftmin[i] - right[i+1]),abs(left[i]-rightmin[i+1]))
        if absvalue > result:
            result = absvalue
    print(result)