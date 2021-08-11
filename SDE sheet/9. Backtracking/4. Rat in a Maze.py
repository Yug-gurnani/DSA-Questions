"""
Consider a rat placed at (0, 0) in a square matrix of order N*N.
It has to reach the destination at (N-1, N-1).
Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and cannot be crossed while value 1 at a cell in the matrix represents that it can be traveled through.

Example 1:

Input: N = 4, m[][] = {{1, 0, 0, 0},
                       {1, 1, 0, 1}, 
                       {1, 1, 0, 0},
                       {0, 1, 1, 1}}
Output: DDRDRR DRDDRR
Explanation: The rat can reach the 
destination at (3, 3) from (0, 0) by two 
paths ie DRDDRR and DDRDRR when printed 
in sorted order we get DDRDRR DRDDRR.
"""
def solve(arr,n,i,j,sol,ans,s):
    if i == n-1 and j == n-1 and arr[i][j] == 1:
        ans.append(s)
        return
    if i < 0 or j < 0 or i >= n or j >= n or arr[i][j] == 0 or sol[i][j] == 1:
        return 
    sol[i][j] = 1
    solve(arr,n,i+1,j,sol,ans,s+"D")
    solve(arr,n,i-1,j,sol,ans,s+"U")
    solve(arr,n,i,j+1,sol,ans,s+"R")
    solve(arr,n,i,j-1,sol,ans,s+"L")
    sol[i][j] = 0
def findPath(arr, n):
    # code here
    ans = []
    sol = [[0 for i in range(n)]for i in range(n)]
    solve(arr,n,0,0,sol,ans,"")
    if ans == []:
        return []
    else:
        ans.sort()
        return ans
"""
TC = o((n^2)^4)
SC = o(L*X) L = length of the maze and X =  number of paths
"""