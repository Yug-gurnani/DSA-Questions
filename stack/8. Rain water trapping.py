def rain_water(arr,n):
    left = []
    right = []
    for i in range(n):
        if not left:
            left.append(arr[i])
        else:
            left.append(max(arr[i],left[-1]))
    for i in range(n-1,-1,-1):
        if not right:
            right.append(arr[i])
        else:
            right.append(max(arr[i],right[-1]))
    right = right[::-1]
    ans = []
    for i in range(n):
        ans.append(min(left[i],right[i]))
    water = 0
    for i in range(n):
        temp = ans[i]-arr[i]
        if temp > 0:
            water += temp
    return water