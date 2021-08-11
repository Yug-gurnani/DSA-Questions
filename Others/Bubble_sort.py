# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:09:35 2020

@author: sam 
"""

def bubble_sort(a):

    for i in range(len(a)):
        for j in range(len(a[1:])):
            if a[i]<a[j]:
                a[i],a[j] = a[j],a[i]
    print(a)
    
bubble_sort([7,10,5,2,9,3])



