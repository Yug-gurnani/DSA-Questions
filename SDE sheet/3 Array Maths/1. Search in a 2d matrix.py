"""
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order,
and a number X is given. The task is to find whether element X is present in the matrix or not.

Example 1:

Input:
N = 3
M = 3
mat[][]: 3 30 38 
         44 52 54 
         57 60 69
X = 62
Output:
0
Explanation: 62 is not present in the
matrix, so output is 0
"""
def searchMatrix(self, arr: List[List[int]], x: int) -> bool:
    r = len(arr)
    c = len(arr[0])
    i = 0
    j = c - 1
    while i < r and j >= 0:
        if arr[i][j] == x:
            return True
        if arr[i][j] > x:
            j -= 1
        elif arr[i][j] < x:
            i += 1
    return False

"""
TC = o(n+m)
SC = o(1)
"""