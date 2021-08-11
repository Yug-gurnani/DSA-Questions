"""
Given a string S and an integer K, the task is to reduce the string by applying the following operation:
Choose a group of K consecutive identical characters and remove them.
The operation can be performed any number of times until it is no longer possible.

Example 1:

Input:
K = 2
S = "geeksforgeeks"
Output:
gksforgks
Explanation:
Modified String after each step: 
"geegsforgeeks" -> "gksforgks

for every push in stack keep the count of occurances and if count reaches k pop from the stack.
"""
from collections import deque
class Solution:
    def Reduced_String(self, k, s):
        if k == 1:
            return ""
        n = len(s)
        ans = ""
        stack = deque([])
        for i in range(n):
            if not stack:
                count = 1
                stack.append([s[i],count])
            else:
                if s[i] == stack[-1][0]:
                    count = stack[-1][1]+1
                    stack.append([s[i],count])
                    if count == k:
                        while count:
                            stack.pop()
                            count -= 1
                else:
                    count = 1
                    stack.append([s[i],count])
        for i in stack:
            ans += i[0]
        return ans