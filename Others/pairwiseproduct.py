# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:58:19 2020

@author: sam
"""
n = int(input())
arr = list(map(int,input().split()))
a = max(arr)
arr.remove(a)
b = max(arr)
print(a*b)
