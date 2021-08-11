# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:22:13 2020

@author: yuggu
"""
for _ in range(int(input())):
    S = input()
    P = input()
    result = ''
    S = list(S)
    P = list(P)
    S.sort()
    if S == sorted(P):
        for i in S:
            result += i
        print(result)
    else:
        count = 0
        for i in P:
            S.remove(i)
            
        for i in S:
            if i <= P[0]:
                result += i
            elif count == 0:
                count = 1
                for j in P:
                    result += j
                result += i
            else:
                result += i
        if count == 0:
            for i in P:
                result += i
                    
        print(result)
    
#aabadawyehhorst
#aaakaeekmnnry