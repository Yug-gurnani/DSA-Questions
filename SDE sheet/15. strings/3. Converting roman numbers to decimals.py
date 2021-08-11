"""

Given a string in roman no format (s)  your task is to convert it to an integer .
Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

Example 1:

Input:
s = V
Output: 5
Example 2:

Input:
s = III 
Output: 3

Approach: A number in Roman Numerals is a string of these symbols written in descending order(e.g. M’s first, followed by D’s, etc.).
However, in a few specific cases, to avoid four characters being repeated in succession(such as IIII or XXXX), subtractive notation is often used as follows: 

I placed before V or X indicates one less, so four is IV (one less than 5) and 9 is IX (one less than 10).
X placed before L or C indicates ten less, so forty is XL (10 less than 50) and 90 is XC (ten less than a hundred).
C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and
nine hundred is CM (a hundred less than a thousand).
"""
def romanToDecimal(s):
    # code here
    dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    res = 0
    i = 0
    n = len(s)
    while i < n:
        s1 = dic[s[i]]
        if i + 1 < n:
            s2 = dic[s[i+1]]
            #print(s1,s2)
            if s1 >= s2:
                res = res + s1
                i += 1
            else:
                res = res + s2 - s1
                i += 2
        else:
            res = res + s1
            i += 1
    return res
"""
TC = o(n)
SC = o(n)
"""