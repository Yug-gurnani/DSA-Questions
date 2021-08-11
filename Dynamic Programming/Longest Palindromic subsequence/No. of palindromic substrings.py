'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
def countSubstrings(self, s):
    n = len(s)
    dp = [[False for i in range(n)]for i in range(n)]
    ans = 0
    # filling all the single elements
    for i in range(n):
        dp[i][i] = True
        ans += dp[i][i]
    #checking the double elements
    for i in range(n-1):
        dp[i][i+1] = s[i] == s[i+1]
        ans += dp[i][i+1]

    #checking the rest of elements of len 3 or more
    for l in range(3,n+1):
        i = 0
        j = i + l - 1
        while j < n:
            dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
            ans += dp[i][j]
            i += 1
            j += 1
    return ans