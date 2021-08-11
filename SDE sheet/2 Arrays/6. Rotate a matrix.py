"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

In this we will first transpose the matrix and then reverse every row to rotate it
"""

def rotate(self, arr: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    n = len(arr)
    # TO transpose the matrix
    for i in range(n):
        for j in range(i):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    #to reverse every row
    for i in range(n):
        arr[i] = arr[i][::-1]