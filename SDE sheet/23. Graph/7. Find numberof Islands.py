"""
Given a grid consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally
i,e in all 8 directions.
 

Example 1:

Input:
grid = {{0,1},{1,0},{1,1},{1,0}}
Output:
1
Explanation:
The grid is-
0 1
1 0
1 1
1 0
All lands are connected.

We do dfs for this and for 1 cell which is land in graph we mark all its adjacent cells as 1 in vis array and then increase the count
so that all lands which are disconnected has their separate count
"""
import sys
sys.setrecursionlimit(100000)
class Solution:
    def dfs(self,graph,vis,i,j):
        row = [-1, -1, -1,  0, 0,  1, 1, 1] 
        col = [-1,  0,  1, -1, 1, -1, 0, 1]
        vis[i][j] = True
        for k in range(8):
            if self.issafe(vis,graph,i + row[k],j + col[k]):
                self.dfs(graph,vis,i+row[k],j + col[k])
    def issafe(self,vis,graph,i,j):
        return i >= 0 and j >= 0 and i < len(vis) and j < len(vis[0]) and not vis[i][j] and graph[i][j] == "1"
	def numIslands(self, grid):
	    r = len(grid)
	    c = len(grid[0])
	    #print(grid)
	    
	    vis = [[False for j in range(c)]for i in range(r)]
	    count = 0
	   
	    for i in range(r):
	        for j in range(c):
	            if not vis[i][j] and grid[i][j] == "1":
	                self.dfs(grid,vis,i,j)
	                count += 1
	    #print(vis)
	    return count