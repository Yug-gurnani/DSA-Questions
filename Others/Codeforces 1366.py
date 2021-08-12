from sys import stdin, stdout
"""
 ____  __.        .__                         
|    |/ _|_____   |  |  ___.__. __ __   ____  
|      <  \__  \  |  | <   |  ||  |  \ / ___\ 
|    |  \  / __ \_|  |__\___  ||  |  // /_/  >
|____|__ \(____  /|____// ____||____/ \___  / 
        \/     \/       \/           /_____/ 
"""
for _ in range(int(stdin.readline())):

    n,x,m = map(int,stdin.readline().split())
    minn = x
    maxx = x
    for i in range(m):
        l,r = map(int,stdin.readline().split())
        if r >= minn and l <= minn:
            maxx = max(maxx, r)
            minn = min(minn, l)
        elif r >= maxx and l <= maxx:
            maxx = max(maxx, r)
            minn = min(minn, l)
    print(maxx - minn + 1)



    

        

