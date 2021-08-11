# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:54:48 2020

@author: sam
"""
def fibo(n):
    i = 0
    j = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    for _ in range(n-1):
        c = i + j     
        i = j
        j = c
        
    print(c)

fibo(12000)

def recfibo(n,a=0,b=1):
    if n == 1:
        return b
    return recfibo(n-1,b,a+b)

#r = recfibo(12000)
#print(r)
