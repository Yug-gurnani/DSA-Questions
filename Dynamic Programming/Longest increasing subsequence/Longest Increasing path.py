"""
Given a two-dimensional integer matrix, find the length of the longest strictly increasing path. You can move up, down, left, or right.

Constraints

n, m ≤ 500 where n and m are the number of rows and columns in matrix
Example 1
Input
matrix = [
    [1, 3, 5],
    [0, 4, 6],
    [2, 2, 9]
]
Output
6
Explanation
The longest path is [0, 1, 3, 5, 6, 9]
"""

class Solution:
    def solve(self, matrix):
        ans,n,m = 0,len(matrix),len(matrix[0])
        
        def issafe(i,j,n,m):
            return i >= 0 and j >= 0 and i < n and j < m
        dp = [[-1 for i in range(m)]for i in range(n)]
        def s(i,j):
            nonlocal matrix
            res = 0
            if dp[i][j] !=-1:
                return dp[i][j]
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if issafe(x,y,len(matrix),len(matrix[0])) and matrix[i][j] < matrix[x][y]:
                    res = max(res,s(x,y))
            dp[i][j] = res+1
            return res + 1

        for i in range(n):
            for j in range(m):
                ans = max(ans,s(i,j))
        
            
        
        return ans