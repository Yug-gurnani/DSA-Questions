"""
Gived a NxM 2D matrix, rearrange such that 
Each diagonal in the lower left triangle of the rectangular grid is sorted in ascending order. 
Each diagonal in the upper right triangle of the rectangular grid is sorted in descending order. 
The major diagonal in the grid starting from the top-left corner is not rearranged. 

Example 1:

Input:
N = 4, M = 5 
matrix = {
    {3 6 3 8 2},
    {4 1 9 5 9},
    {5 7 2 4 8},
    {8 3 1 7 6}
}
Output: {
    {3 9 8 9 2}
    {1 1 6 5 8}
    {3 4 2 6 3}
    {8 5 7 7 4}
}
"""
from collections import defaultdict,deque
class Solution:
    def diagonalSort(self, mat, n, m):
        # code here
        neg = defaultdict(deque)
        pos = defaultdict(deque)
        
        for i in range(n):
            for j in range(m):
                if j > i:
                    pos[j-i].append(mat[i][j])
                elif j < i:
                    neg[i-j].append(mat[i][j])
                else:
                    pos[0].append(mat[i][j])
        for i in pos:
            if i != 0:
                pos[i] = deque(sorted(pos[i]))
        for i in neg:
            neg[i] = deque(sorted(neg[i]))
        for i in range(n):
            for j in range(m):
                if j > i:
                    d = j - i
                    tmp = pos[d].pop()
                    mat[i][j] = tmp
                elif j < i:
                    d = i-j
                    tmp = neg[d].popleft()
                    mat[i][j] = tmp
                else:
                    tmp = pos[0].popleft()
                    mat[i][j] = tmp
"""
TC = o(n*m)
"""