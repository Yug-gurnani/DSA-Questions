def ceil(arr,l,r,key):
    while r-l > 1:
        m = l + (r-l)//2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r
arr = []
tail = [0 for i in range(len(arr)+ 1)]
l = 0
tail[0] = arr[0]
l = 1
for i in range(1,len(arr)):
    if arr[i] < tail[0]:
        tail[0] = arr[i]
    elif arr[i] > tail[l-1]:
        tail[l] = arr[i]
        l += 1
    else:
        c = ceil(tail,-1,l-1,arr[i])
        tail[c] = arr[i]
print(l)