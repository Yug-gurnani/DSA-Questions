# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return len(results)
print(all_repeat("012345",3))
