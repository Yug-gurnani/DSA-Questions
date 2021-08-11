"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

we use the sliding window + hashing technique in this.
"""

def solve(s):
    n = len(s)
    i = 0
    j = 0
    dic = {}
    ans = []
    while j < n:
        if s[j] not in dic:
            dic[s[j]] = 1
            j += 1
        else:
            ans.append(j-i)
            while s[i] != s[j]:
                del dic[s[i]]
                i += 1
            del[dic[s[i]]]
            dic[s[j]] = 1
            i += 1
            
            j += 1
    ans.append(j-i)
    if ans == []:
        print(n)
    else:
        #print(ans)
        print(max(ans))

"""
TC = o(n)
SC = o(1)
"""