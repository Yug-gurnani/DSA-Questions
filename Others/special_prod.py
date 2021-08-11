# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:20:52 2020

@author: yuggu
"""
a = [1,2,3,4,5]
def special_prod(a):
    left = [1] *(len(a)+2)
    right = [1] * (len(a)+2)
    output = [1] * len(a)
    for i in range(len(a)):
        left[i] = a[i] * left[i-1]
        
    for i in range(len(a)-1,0,-1):
        right[i] = a[i] * right[i+1]
        
    for i in range(len(a)):
        output[i] = left[i-1] * right[i+1]
        
    for i in output:
        print(i)
        
special_prod(a)
