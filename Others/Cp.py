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

    n = int(stdin.readline())
    
    arr = []
    arr.append(list(map(stdin.readline().split())))
    arr.append(list(map(stdin.readline().split())))

    bob = 0
    alice = 0

    dp = [[0 for i in range(n+1)] for i in range(3)]

    

