"""
Given a positive integer, write a function to find if it is a power of two or not.
Examples : 

Input : n = 4
Output : Yes
22 = 4

Input : n = 7
Output : No

Input : n = 32
Output : Yes
25 = 32

Algo - If we subtract a power of 2 numbers by 1 then all unset bits after the only set bit become set; and the set bit becomes unset.
For example for 4 ( 100) and 16(10000), we get the following after subtracting 1 
3 –> 011 
15 –> 01111

So, if a number n is a power of 2 then bitwise & of n and n-1 will be zero. We can say n is a power of 2 or not based on the value of n&(n-1).
The expression n&(n-1) will not work when n is 0. To handle this case also, our expression will become n& (!n&(n-1))
"""
def ispoweroftwo(x):
    if x == 0:
        return False
    else:
        if x & (x-1) == 0:
            return True
        return False
print(ispoweroftwo(0))