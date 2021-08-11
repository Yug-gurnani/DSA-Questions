# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:13:18 2020

@author: yuggu
"""
T = int(input())
while T:
    n = int(input())
    arr = list(map(str,input().split()))
   
    
    c = 0
    i = 0
    
    while i < n:
        if arr[i] == "1":
            c+=1
            pass
        else:
            if c%2 != 0:
                
                del arr[i-1]
                i-=1
                n-=1
            c = 0        
        i+=1
    if c%2 != 0:
        del arr[-1]
                
                
    print(len(arr))       
    print(*arr)
            
            
            
            
    T-=1