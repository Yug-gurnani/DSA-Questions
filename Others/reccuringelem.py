# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:43:38 2020

@author: sam
"""

a = [22,1,3,9,4,6,5,7,8,1,22,1]
b =[1,5,2,3,4,5,1]


def naive(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    return None
        


def checkReccurence(arr):
    d = {}
    for i in arr:
        if i in d:
            return i
        else:
            d[i] =  True
        
#res = checkReccurence(a)
res = naive(b)
print(res)

        