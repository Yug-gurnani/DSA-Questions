"""
https://codeforces.com/contest/1554/problem/A
"""
"""
 ____  __.        .__                         
|    |/ _|_____   |  |  ___.__. __ __   ____  
|      <  \__  \  |  | <   |  ||  |  \ / ___\ 
|    |  \  / __ \_|  |__\___  ||  |  // /_/  >
|____|__ \(____  /|____// ____||____/ \___  / 
        \/     \/       \/           /_____/ 
"""
from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int,stdin.readline().split()))
    ans = 0
    for i in range(n-1):
        ans = max(ans,arr[i] * arr[i+1])

    print(ans)