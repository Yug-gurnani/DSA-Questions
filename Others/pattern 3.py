# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:58:19 2020

@author: sam
"""
n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(end = " ")
    for j in range(i):
        print("#",end = " ")
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
        print(end = " ")
    for j in range(i):
        print("#",end = " ")
    
    print()

