"""
Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9 .


Example 1:
 

Input:
N = 8
Output:
8
Explanation:
After removing natural numbers which contains
digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
and 8th number is 8.

Approach is to simply return the base 9 of that number
"""
def findNth(self,n):
    #code here
    ans = ""
    while n != 0:
        tmp = n//9
        tmp1 = n%9
        n = tmp
        ans += str(tmp1)
    return int(ans[::-1])
"""
TC - O(log n)
SC - O(1)
"""