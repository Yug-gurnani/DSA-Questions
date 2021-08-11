for _ in range(int(input())):
    n,x,p,k = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = sorted(arr)
    if brr[p-1] == x:
        print(0)
    elif p == k:
        print(1)
    else:
        if x in arr:
            steps = 0
            prevk = None
            while True:
                if prevk == brr[k-1]:
                    print(-1)
                    break
                prevk = brr[k-1]
                if brr[p-1] == x:
                    print(steps)
                    break
                try:
                    temp = brr.index(x)
                except:
                    print(-1)
                    break
                
                if temp < p-1:
                    brr[k-1] = x-1
                    steps += 1
                else:
                    brr[k-1] = x+1
                    steps += 1
                brr.sort()
        else:
            if not p == k:
                print(-1)

             