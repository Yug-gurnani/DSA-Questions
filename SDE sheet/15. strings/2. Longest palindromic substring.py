"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""
def longestPalindrome(s: str) -> str:
    n = len(s)
    new = "#"
    for i in range(n):
        new += s[i]
        new += "#"
    maxlen = 0
    ans = ""
    s = new
    n = len(s)
    for k in range(1,n-1):
        if s[k-1] == s[k+1]:
            i = k - 1
            j = k + 1
            while i > 0 and j < n-1 and s[i] == s[j]:
                i -= 1
                j += 1
            curr = 0
            temp = ""
            for t in range(i+1,j):
                if s[t] != "#":
                    temp += s[t]
                    curr += 1
            if curr > maxlen:
                maxlen = curr
                ans = temp
    s = ""
    for i in ans:
        if i != "#":
            s += i
    return s
"""
TC = o(n^2)
SC = o(n)
"""