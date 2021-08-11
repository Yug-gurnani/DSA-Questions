# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:08:38 2020

@author: sam
"""
counter = 0
f=1
def fact(a):
    global counter
    global f
    f = f * a
   
    if counter>a:
        return
    counter +=1
    fact(a-1)
    return f
    
    
    
    
    

        


g = fact()
print(g)