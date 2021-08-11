# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:09:27 2020

@author: yuggu
"""
def findGolomb(n,memo):
  
    # base case 
    if (n == 1): 
        return 1
    
  
    # Recursive Step 
    if n in memo:
        return memo[n]
    
        
        
    
    result = 1 + findGolomb(n -
    findGolomb(findGolomb(n - 1,memo),memo),memo) 
    
    memo[n] = result
    
    return result
  
  
# Print the first n term  
# of Golomb Sequence 
def printGolomb(k,n): 
  
    # Finding first n terms of 
    # Golomb Sequence. 
    r = []
    for i in range(k, n + 1):  
        r.append(findGolomb(i,{}))
        
    return r
T = int(input())
while T:
    k,n = map(int,input().split())
    a = printGolomb(k,n)
    s = 0
    for i in a:
        s += i**2
        
    print(s)
    
    T -= 1
    
        
        

