"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dic = {}
    dic2 = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
        if t[i] not in dic2:
            dic2[t[i]] = 1
        else:
            dic2[t[i]] += 1
    return dic == dic2
"""
TC = o(n)
SC = o(n)
"""