class Box:
    def __init__(self,w,h,d):
        self.w = w
        self.h = h
        self.d = d
def maxHeight(h, w, l, n):
    arr = [Box(0,0,0) for i in range(n*3)]
    index = 0
    for i in range(n):
        arr[index].h = h[i]
        arr[index].w = max(w[i],l[i])
        arr[index].d = min(w[i],l[i])
        index += 1
        
        arr[index].h = w[i]
        arr[index].w = max(h[i],l[i])
        arr[index].d = min(h[i],l[i])
        index += 1
        
        arr[index].h = l[i]
        arr[index].w = max(w[i],h[i])
        arr[index].d = min(w[i],h[i])
        index += 1
        
    n *= 3
    arr.sort(reverse = True,key = lambda x:x.w)
    dp = [0]*n
    for i in range(n):
        dp[i] = arr[i].h
    for i in range(1,n):
        for j in range(0,i):
            if arr[i].w < arr[j].w and arr[i].d < arr[j].d and dp[i] < dp[j] + arr[i].h:
                dp[i] = dp[j] + arr[i].h
    #print(dp)
    maxm = -1
    maxm = max(maxm,max(dp))
    return maxm