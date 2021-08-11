"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

In this we used bfs and we keep adding all the rotten oranges till the end and then sees if there is some fresh orange left or not
"""
from collections import deque
def orangesRotting(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    class ele:
        def __init__(self,x,y,timeframe):
            self.x = x
            self.y = y
            self.t = timeframe
        
    q = deque([])
    def isvalid(i,j,m,n):
        if i >= 0 and j >= 0 and i < m and j < n:
            return True
        return False
    def check(grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                temp = ele(i,j,0)
                q.append(temp)
    ans = 0
    while q:
        temp = q[0]
        ans = max(temp.t,ans)
        if isvalid(temp.x+1,temp.y,m,n) and grid[temp.x+1][temp.y] == 1:
            q.append(ele(temp.x+1,temp.y,temp.t+1))
            grid[temp.x+1][temp.y] = 2
        if isvalid(temp.x-1,temp.y,m,n) and grid[temp.x-1][temp.y] == 1:
            q.append(ele(temp.x-1,temp.y,temp.t+1))
            grid[temp.x-1][temp.y] = 2
        if isvalid(temp.x,temp.y+1,m,n) and grid[temp.x][temp.y+1] == 1:
            q.append(ele(temp.x,temp.y+1,temp.t+1))
            grid[temp.x][temp.y+1] = 2
        if isvalid(temp.x,temp.y-1,m,n) and grid[temp.x][temp.y-1] == 1:
            q.append(ele(temp.x,temp.y-1,temp.t+1))
            grid[temp.x][temp.y-1] = 2
        q.popleft()
    if check(grid):
        return -1
    else:
        return ans
"""
TC = o(n*m)
SC = o(n)
"""