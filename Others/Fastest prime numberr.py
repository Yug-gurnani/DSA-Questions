# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:52:44 2020

@author: yuggu
"""
#import tensorflow as tf
from collections import OrderedDict
def generate_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    ans = OrderedDict()
    for p in range(2, n+1):
        if prime[p]:
            ans[p] = 1
    return ans
primes = generate_primes(10**9)
print(primes)