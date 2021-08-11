# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:40:32 2020

@author: yuggu
"""
def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)
print(gcd(1,7))