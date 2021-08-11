# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:31:30 2020

@author: sam
"""
a = [4,2,1,10,8,3,10]
b = []
for i in range(len(a)):
    c = min(a)
    b.append(c)
    a.remove(c)
    
print(b)

