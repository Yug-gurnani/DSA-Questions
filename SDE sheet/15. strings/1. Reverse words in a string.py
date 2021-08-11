"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

we use two pointer approach and make pointer i and j to slice a word and add it to result

we use extra space because string is immutable in python
"""
def reverseWords(self, s: str) -> str:
    res = ""
    i = 0
    j = 0
    n = len(s)
    while j < n:
        temp = ""
        while i < n and s[i] == " ":
            i += 1
        j = i
        while j < n and s[j] != " ":
            temp += s[j]
            j += 1
        i = j
        if not res:
            res = temp[:]
        else:
            if temp:
                res = temp + " " + res
    return res
"""
TC = o(n)
SC = o(n)
"""
    