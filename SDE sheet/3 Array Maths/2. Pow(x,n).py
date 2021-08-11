"""
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

There are two approachs:
one work only in python
and other works in any language
"""
#1st
def solve(x,n):
    return x**n
#2nd
def solve(x,n):
    nn = n
    if n < 0:
        n = -1 * n
    
    ans = 1
    while n:
        if n %2 == 1:
            ans = ans * x
            n -= 1
        else:
            x = x * x
            n = n//2
    if nn <0:
        ans = 1 / ans
    return ans