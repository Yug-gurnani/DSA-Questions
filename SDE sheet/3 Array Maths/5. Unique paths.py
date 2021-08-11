"""
It is more of a dp problem in which robot can only move in a right or bottom direction

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

def uniquePaths(self, m: int, n: int) -> int:
    arr = [[0 for i in range(n)]for i in range(m)]
    for i in range(m):
        arr[i][0] = 1
    for i in range(n):
        arr[0][i] = 1
    for i in range(1,m):
        for j in range(1,n):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr[m-1][n-1]
"""
TC = o(m*n)
SC = o(m*n)
"""

"""
But there is one more optimized solution of this

As we can observe that we have fixed size of moves :
m-1 right moves
n-1 down moves
so by observing we can see that it is a combanatrics problem and
we can find its solution by NCR method
"""
def solve(m,n):
    N = m + n - 2 # m - 1 right and n - 1 down moves
    r = m - 1
    res = 1
    for i in range(1,r+1):
        res *= (N-r+i) / i
    return int(res)
"""
TC = o(n)
SC = o(1)
"""
