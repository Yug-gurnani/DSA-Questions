# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:34:29 2020

@author: yuggu
"""


def merge_sorting_array():
    c = [1,9,7,64,5,3]
    d = [1,3,7,64,5,9]
    for i in range(len(c)-1):
        for j in range(i+1,len(c)):
            if c[i]>c[j]:
                temp = c[i]
                c[i] = c[j]
                c[j] = temp
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            if d[i]>d[j]:
                temp = d[i]
                d[i] = d[j]
                d[j] = temp
    a = c+d
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a