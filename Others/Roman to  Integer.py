# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:06:38 2020

@author: sam
"""

    def romanToInt(s):
        result = 0
        for i in range(len(s)):
            if s[i] == 'I':
                result += 1
            if s[i] == 'V':
                if i == 0:
                    result +=5
                else:
                    
                    if s[i-1] == 'I':
                        result += 3
                    else:
                        result += 5
            if s[i] == 'X':
                if i == 0:
                    result += 10
                else:
                    if s[i-1] == 'I':
                        result += 8
                    else:
                        result += 10
            if s[i] == 'L':
                if i == 0:
                    result += 50
                else:
                    
                    if s[i-1] == 'X':
                        result += 30
                    else:
                        result += 50
            if s[i] == 'C':
                if i == 0:
                    result += 100
                else:
                    if s[i-1] == 'X':
                        result += 80
                    else:
                        result += 100
            if s[i] == 'D':
                if i == 0:
                    result += 500
                else:
                    
                    if s[i-1] == 'C':
                        result += 300
                    else:
                        result += 500
            if s[i] == 'M':
                if i == 0:
                    result +=1000
                else:
    
                    if s[i-1] == 'C':
                        result += 800
                    else:
                        result += 1000
            print(result)
        return result
        
        



