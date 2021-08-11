# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:44:49 2020

@author: sam
"""
a = 'ababababababa'
n = len(a)//2
x = []
y = []
for i in a[:n]:
    x.append(i)
    
if len(a)%2==0:
    
    for i in a[n:]:
        y.append(i)
else:
    for i in a[n+1:]:
        y.append(i)
for i in range(n):   
    if x == y:
        print(len(x))
        break
    if x !=[]:
        x.pop()
    if y !=[]:
        y.pop(0)
else:
    print('0')
