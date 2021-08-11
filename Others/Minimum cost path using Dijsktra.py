"""
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j). 

Note: It is assumed that negative cost cycles do not exist in the input matrix.
 

Example 1:

Input: grid = {{9,4,9,9},{6,7,6,4},
{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
"""
from heapq import heappush,heappop
class Solution:
	def minimumCostPath(self, grid):
	    def isvalid(i,j,n):
	        return i >= 0 and j >= 0 and i < n and j < n
		#Code here
		heap = []
		heappush(heap,[grid[0][0],0,0])
		n = len(grid)
		vis = {}
		while heap:
		    currcost,i,j = heappop(heap)
		    if (i,j) in vis:
		        continue
		    else:
		        vis[(i,j)] = 1
		    if i == j == n-1:
		        return currcost
		    
		    if isvalid(i,j-1,n):
		        heappush(heap,[currcost + grid[i][j-1],i,j-1])
		    if isvalid(i,j+1,n):
		        heappush(heap,[currcost + grid[i][j+1],i,j+1])
		    if isvalid(i-1,j,n):
		        heappush(heap,[currcost + grid[i-1][j],i-1,j])
		    if isvalid(i+1,j,n):
		        heappush(heap,[currcost + grid[i+1][j],i+1,j])