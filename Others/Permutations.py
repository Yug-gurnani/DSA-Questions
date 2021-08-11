# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:30:45 2020

@author: yuggu
"""

from itertools import permutations  
  
  
a = "123456789012345678901234567890"
  
# no length entered so default length 
# taken as 4(the length of string GeEK) 
p = permutations(a)  
  
# Print the obtained permutations  
for j in list(p):  
    print(j)  