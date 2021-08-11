"""
Flamel is making the Elixir of Life but he is missing a secret ingredient, a set of contiguous plants (substring) from the Garden of Eden. The garden consists of various plants represented by string S where each letter represents a different plant.  But the prophecy has predicted that the correct set of plants required to make the potion will appear in the same contiguous pattern (substring) at the beginning of the forest (prefix), the end of the forest (suffix), and will also be the most frequent sequence present in the entire forest.

Identify the substring of plants required to make the elixir and find out the number of times it appears in the forest. 

Example 1:

Input: S = "ababaaaab"
Output: 3
Explanation: substring "ab" is a prefix, 
a suffix and appears 3 times.
"""
class Solution:
    def maxFrequency(self, s):
        # code here
        n = len(s)
        s1 = ""
        for i in s:
            if i not in s1:
                s1 += i
                if s == s1:
                    return 1
        tmp = ""
        c = 0
        for i in range(1,n):
            if s[:i] == s[n-i:n]:
                tmp = s[:i]
                break
            else:
                tmp = s
        c = s.count(tmp)
        return c
"""
TC = o(n log n)
SC = o(n)
"""