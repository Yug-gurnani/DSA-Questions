# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:23:05 2020

@author: sam
"""

a = [-1,-2,-3,-5,-2]
def kadane(a):
    max_current = max_global = a[0]
    for i in range(1,len(a)):
        max_current = max(a[i],max_current + a[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global

print(kadane(a))

