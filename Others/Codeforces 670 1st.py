# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 19:39:49 2020

@author: yuggu
"""
def mex(arr):
    if arr == []:
        return 0
    arr.sort()
    res = None
    for i in range(len(arr)):
        #print(arr[i],i)
        if arr[i] != i:
            res = i
            break
    if res == None:
        res = len(arr)
    return res
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    a = []
    b = []
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    for i in dic:
        if dic[i] > 1:
            a.append(i)
            b.append(i)
            dic[i] = 0
        else:
            a.append(i)
            dic[i] = 0
    #print(a,b)
    x = mex(a)
    y = mex(b)
    print(x+y)