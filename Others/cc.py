# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:57:33 2020

@author: yuggu
"""

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if arr[i] > 0 and arr[i+1] < 0:
            a = abs(arr[i+1])
            if arr[i] > a:
                arr[i] -= a
                arr[i+1] = 0
            elif arr[i] < a:
                arr[i+1] += arr[i]
                arr[i] = 0
    temp = 0
    for i in arr:
        if i > 0:
            temp += i
    
        