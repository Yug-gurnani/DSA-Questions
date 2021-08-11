"""
Given a non-negative integer S represented as a string, remove K digits from the number so that the new number is the smallest possible.
Note : The given num does not contain any leading zero

S = "1002991", K = 3
Output: 21
Explanation: Remove the three digits
1(leading one), 9, and 9 to form the 
new number 21(Note that the output 
must not contain leading zeroes) 
which is the smallest.
"""

#User function Template for python3p
class Solution:
    def removeKdigits(self, s, k):
        stack = []
        ans = 0
        for i in range(len(s)):
            while stack and k and s[i] < stack[-1]:
                k -= 1
                stack.pop()
            stack.append(s[i])
        while k:
            stack.pop()
            k -= 1
        for i in stack:
            ans = ans * 10 + int(i)
        return ans