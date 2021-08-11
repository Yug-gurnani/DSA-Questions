# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:44:23 2020

@author: sam
"""




for i in range(int(input())):

    chef = 0
    morty = 0
    
    for j in range(int(input())):
        c,m = input().split()
        c_val = 0
        m_val = 0
        for k in c:
            c_val+= int(k)
        for _ in m:
            m_val += int(_)
        if c_val>m_val:
            chef += 1
        elif c_val<m_val:
            morty += 1
        elif c_val == m_val:
            chef +=1
            morty += 1
        
    if chef > morty:
        print('0 ',chef)
    elif  chef < morty:
        print('1 ',morty)
    else:
        print('2 ',chef)
        
        
        