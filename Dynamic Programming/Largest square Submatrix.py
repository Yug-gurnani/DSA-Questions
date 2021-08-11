"""
Given a binary matrix mat of size n * m, find out the maximum size square sub-matrix with all 1s.

Example 1:

Input: n = 2, m = 2
mat = {{1, 1}, 
       {1, 1}}
Output: 2
Explaination: The maximum size of the square
sub-matrix is 2. The matrix itself is the 
maximum sized sub-matrix in this case.
"""
class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        ans = 0
        dp = [[0 for i in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = mat[i][j]
                else:
                    if mat[i][j] == 1:
                        dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                ans = max(ans,dp[i][j])
        
        return ans
"""
TC = o(nm)
SC = o(nm)
"""