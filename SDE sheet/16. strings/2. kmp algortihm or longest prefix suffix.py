"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel").
The largest prefix which is also suffix is given by "l".

In this we used the preprocessing of KMP algorithm to find the lps and then we find out the longest happy prefix
"""
def longestPrefix(self, s: str) -> str:
    def makelps(pat):
        m = len(pat)
        lps = [0] * m
        i = 1
        j = 0
        while i < m:
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    lps = makelps(s)
    ans = lps[-1]
    print(lps)
    for i in range(len(lps)):
        if s[i] == ans:
            break
    temp = ""
    while ans:
        temp += s[i]
        ans -= 1
        i -= 1
    return temp[::-1]
"""
TC = o(n)
SC = o(n)
"""