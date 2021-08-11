# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:43:10 2020

@author: sam
"""

#IN case of sorted array
#TIME complexity O(n)
a = [3,6,6,8,10,13,14]
b = [1,2,6,6,10,13,15]
c = [2,3,6,6,9,11,13] 
def commomvalues(a,b,c):
    result = []
    x = 0
    y = 0
    z = 0
    def base():
        return x >= len(a) or y >= len(b) or z >= len(c)
    
    while not base():
        if a[x] == b[y] == c[z]:
            result.append(a[x])
            x += 1
            y += 1
            z += 1
            
        elif a[x]<b[y]:
            x += 1
        elif b[y]<c[z]:
            y += 1
        else:
            z += 1
    return result

print(commomvalues(a,b,c))
            

#IN case of non sorted array
#TIME complexity O(n log n)
a = [5,1,7,3,8,1,3,15]
b = [5,2,7,3,6,19,3,15]
c = [5,3,12,3,9,10,3,15] 
def commomvalues_non_sorted(a,b,c):
    a.sort()
    b.sort()
    c.sort()
    
    result = []
    x = 0
    y = 0
    z = 0
    def base():
        return x >= len(a) or y >= len(b) or z >= len(c)
    
    while not base():
        if a[x] == b[y] == c[z]:
            result.append(a[x])
            x += 1
            y += 1
            z += 1
            
        elif a[x]<b[y]:
            x += 1
        elif b[y]<c[z]:
            y += 1
        else:
            z += 1
    return result

print(commomvalues_non_sorted(a,b,c))
    