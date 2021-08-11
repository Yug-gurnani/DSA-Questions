from bisect import bisect_right as upper_bound 
def median( arr, r, c):
    mn = float('inf')
    mx = -float('inf')
    for i in range(r):
        mn = min(arr[i][0],mn)
        mx = max(arr[i][-1],mn)
    #print(mn,mx)
    des = (r*c+1)//2
    while mn < mx:
        temp = 0
        mid = mn + (mx - mn)//2
        #print(mn,mx)
        for i in range(r):
            
            j = upper_bound(arr[i],mid)
            #print(j,mid)
            temp += j
        if temp < des:
            mn = mid + 1
        else:
            mx = mid
    return mn