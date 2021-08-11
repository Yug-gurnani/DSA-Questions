# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:41:38 2020

@author: sam
"""

a=[1,9,100,4,-1,6,0,1231,42,14,4,3434,24,24,4]
b = []
while a:
    c  = min(a)
    a.remove(c)
    b.append(c)
print(b)
    

