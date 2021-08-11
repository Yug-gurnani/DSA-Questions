"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
def minCut(self, s: str) -> int:
    n = len(s)
    dp = [[-1 for i in range(n+1)]for i in range(n+1)]
    def solve(s,i,j,ans):
        nonlocal dp
        if i >= j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        tmp = s[i:j+1]
        if tmp == tmp[::-1]:
            return 0
        for k in range(i,j):
            tmp = solve(s,i,k,ans) + solve(s,k+1,j,ans) + 1
            if tmp < ans:
                ans = tmp
        dp[i][j] = ans
        return dp[i][j]

    ans = float('inf')
    return solve(s,0,len(s),ans)
"""
TC = o(n*n)
SC = o(n*n)
"""