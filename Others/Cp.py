"""
 ____  __.        .__                         
|    |/ _|_____   |  |  ___.__. __ __   ____  
|      <  \__  \  |  | <   |  ||  |  \ / ___\ 
|    |  \  / __ \_|  |__\___  ||  |  // /_/  >
|____|__ \(____  /|____// ____||____/ \___  / 
        \/     \/       \/           /_____/ 
"""
 
from sys import stdin, stdout
from collections import defaultdict
n,m = map(int,stdin.readline().split())
dic = {}
survivors = n
for i in range(1,n+1):
    dic[i] = {}
for i in range(m):
    u,v = map(int,stdin.readline().split())
 
    if u > v:
        if len(dic[v]) == 0:
            survivors -= 1
        dic[v][u] = 1
        
 
    elif v > u:
        if len(dic[u]) == 0:
            survivors -= 1
        dic[u][v] = 1
 
q = int(input())
for i in range(q):
    temp = list(map(int,stdin.readline().split()))
    if temp[0] == 3:
        print(survivors)
    else:
        type,u,v = temp
        if type == 1:
            if u > v:
                if len(dic[v]) == 0:
                    survivors -= 1
                dic[v][u] = 1
        
 
            elif v > u:
                if len(dic[u]) == 0:
                    survivors -= 1
                dic[u][v] = 1
        elif type == 2:
            if u > v:
                del dic[v][u]
                if len(dic[v]) == 0:
                    survivors += 1
            else:
                del dic[u][v]
                if len(dic[u]) == 0:
                    survivors += 1