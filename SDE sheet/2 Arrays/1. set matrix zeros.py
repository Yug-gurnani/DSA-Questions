"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    r = len(matrix)
    c = len(matrix[0])
    iscol = False
    for i in range(r):
        if matrix[i][0] == 0:
            iscol = True
        for j in range(1,c):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    
    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(c):
            matrix[0][j] = 0
    if iscol: #for checking the first column needs to be turned or not
        for i in range(r):
            matrix[i][0] = 0