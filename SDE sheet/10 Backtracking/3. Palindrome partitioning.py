"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""
def partition(self, s: str) -> List[List[str]]:
    def backtrack(s,point,comb,res):
        if point == len(s):
            res.append(comb[:])
            return
        else:
            for i in range(point,len(s)):
                sub = s[point:i+1]
                if sub == sub[::-1]:
                    comb.append(sub)
                    backtrack(s,i+1,comb,res)
                    comb.pop()
    
    res = []
    backtrack(s,0,[],res)
    return res
"""
TC = o(2^n)
SC = o(1)
"""