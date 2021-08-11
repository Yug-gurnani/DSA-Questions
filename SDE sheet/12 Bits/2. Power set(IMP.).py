"""
Given a string S find all possible substrings of the string in lexicographically-sorted order.

Example 1:

Input : str = "abc"
Output: a ab abc ac b bc câ€‹
Explanation : There are 7 substrings that 
can be formed from abc.
Example 2:

Input: str = "aa"
Output: a a aa
Explanation : There are 3 substrings that 
can be formed from aa.

Another version other than recursion

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
"""
def AllPossibleStrings(self, s):
    # Code here
    ans = []
    n = len(s)
    for count in range(1,2**n):
        temp = ""
        c = bin(count)[2:]
        c = c[::-1]
        #print(c)
        for j in range(len(c)):
            if c[j] == "1":
                temp += s[j]
        ans.append(temp)
    return sorted(ans)
"""
TC = o(2^n)
SC = o(2^n)
"""