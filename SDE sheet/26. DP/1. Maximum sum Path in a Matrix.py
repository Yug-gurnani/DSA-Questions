"""
Given an n*m matrix, the task is to find the maximum sum of elements of cells starting from the cell (0, 0) to cell (n-1, m-1). 
However, the allowed moves are right, downwards or diagonally right, i.e, from location (i, j) next move can be (i+1, j), or, (i, j+1), or (i+1, j+1). Find the maximum sum of elements satisfying the allowed moves.
Examples: 

Input:
mat[][] = {{100, -350, -200},
           {-100, -300, 700}}
Output: 500
Explanation: 
Path followed is 100 -> -300 -> 700
"""
def maximum_path_sum(mat,vis,dp,i,j):
    n = len(mat)
    m = len(mat[0])
    if i == n-1 and j == m - 1:
        dp[i][j] = mat[i][j]
        return dp[i][j]
    if vis[i][j]:
        return dp[i][j]
    vis[i][j] = 1
    total_sum = dp[i][j]

    if i < n-1 and j < m-1:
        currentsum = max(maximum_path_sum(mat,vis,dp,i,j+1),maximum_path_sum(mat,vis,dp,i+1,j+1),maximum_path_sum(mat,vis,dp,i+1,j))
        total_sum = currentsum + mat[i][j]
        dp = total_sum
    elif i == n-1:
        total_sum = mat[i][j] + maximum_path_sum(mat,vis,dp,i,j+1)
        dp[i][j] = total_sum
    else:
        total_sum = mat[i][j] + maximum_path_sum(mat,vis,dp,i+1,j)
        dp[i][j] = total_sum
    return total_sum
"""
TC = o(n*m)
SC = o(n*m)
"""