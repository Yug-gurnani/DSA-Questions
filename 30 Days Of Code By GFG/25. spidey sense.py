"""
Spiderman is stuck in a difficult situation. His arch-enemy the Green Goblin has planted several
of his infamous Pumpkin Bombs in various locations in a building. Help Spiderman activate his Spidey Sense
and identify the impact zones. 
He has a blueprint of the building which is a M x N matrix that is filled with the characters ‘O’, ‘B’, and ‘W’ where: 
‘O’ represents an open space.
‘B’ represents a bomb.
‘W’ represents a wall.
You have to replace all of the O’s (open spaces) in the matrix with their shortest distance from a bomb
without being able to go through any walls. Also, replace the bombs with 0 and walls with -1 in the resultant matrix.
If no path exists between a bomb and an open space replace the corresponding 'O' with -1.

Example 1:

Input: N = 3, M = 3
A[] = {{O, O, O}, 
       {W, B, B}, 
       {W, O, O}}
Output: {{2, 1, 1}, 
         {-1, 0, 0},  
         {-1, 1, 1}}
Explanation: The walls at (1,0) and (2,0) 
are replaced by -1. The bombs at (1,1) and 
(1,2) are replaced by 0. The impact zone 
for the bomb at (1,1) includes open spaces 
at index (0,0), (0,1) and (2,1) with distance 
from bomb calculated as 2,1,1 respectively.
The impact zone for the bomb at (1,2) 
includes open spaces at index (0,3) and (2,2) 
with distance from bomb calculated as 1,1 
respectively.
"""
from collections import deque

class Solution:
    def findDistance(self, mat, m, n):
        # Your code goes here
        def issafe(i,j,m,n,mat):
            return i >= 0 and j >= 0 and i < m and j < n and mat[i][j] != -1 and mat[i][j] != 0
        q = deque()
        check = [[False for i in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "W":
                    check[i][j] = True
                    mat[i][j] = -1
                elif mat[i][j] == "B":
                    q.append([i,j,0])
                    check[i][j] = True
                    mat[i][j] = 0
                else:
                    mat[i][j] = float("inf")
        
        while q:
            curr = q.popleft()
            i,j = curr[0],curr[1]
            
            
            
            if issafe(i-1,j,m,n,mat):
                mat[i-1][j] = min(mat[i-1][j],curr[2] + 1)
                if not check[i-1][j]:
                    check[i-1][j] = True
                    q.append([i-1,j,mat[i-1][j]])
                else:
                    check[i-1][j] = True
                    
                    
                    
            if issafe(i+1,j,m,n,mat):
                mat[i+1][j] = min(curr[2] + 1,mat[i+1][j])
                if not check[i+1][j]:
                    check[i+1][j] = True
                    q.append([i+1,j,mat[i+1][j]])
                else:
                    check[i+1][j] = True
                    
                    
                    
            if issafe(i,j-1,m,n,mat):
                mat[i][j-1] = min(curr[2] + 1,mat[i][j-1])
                if not check[i][j-1]:
                    check[i][j-1] = True
                    q.append([i,j-1,mat[i][j-1]])
                else:
                    check[i][j-1] = True
                    
                    
            if issafe(i,j+1,m,n,mat):
                mat[i][j+1] = min(curr[2] + 1,mat[i][j+1])
                if not check[i][j+1]:
                    check[i][j+1] = True
                    q.append([i,j+1,mat[i][j+1]])
                else:
                    check[i][j+1] = True
                    
                    
        for i in range(m):
            for j in range(n):
                if mat[i][j] == float("inf"):
                    mat[i][j] = -1
        return mat
"""
TC = o(m*n)
SC = o(m*n)
"""