# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:58:36 2020

@author: sam
"""

test = int(input())
for i in range(test):
    n = int(input())
    array = tuple(map(int,input().split()))
    maxx = max(array)
    count = 0
    set1 = set(array)
    for j in range(n):
        
        if len(set1) == 1:
            break
        if array[j] == maxx:
            count += 1
            break
        if array[j+1] < 2:
            count += 1
    print("Case #{}: {}".format(i+1,count))
