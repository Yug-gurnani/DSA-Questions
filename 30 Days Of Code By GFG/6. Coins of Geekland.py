"""
In Geekland there is a grid of coins of size N x N. You have to find the maximum sum of coins in any sub-grid of size K x K.
Note: Coins of the negative denomination are also possible at Geekland.

Example 1:

Input: N = 5, K = 3 
mat[[]] = {1, 1, 1, 1, 1} 
          {2, 2, 2, 2, 2} 
          {3, 8, 6, 7, 3} 
          {4, 4, 4, 4, 4} 
          {5, 5, 5, 5, 5}
Output: 48
Explanation: {8, 6, 7}
             {4, 4, 4}
             {5, 5, 5}
has the maximum sum

Let the matrix be 5X5 and K=3X3. First, calculate the sum of three consecutive elements of each col, the new matrix that you will get is 5X3 (no. of col i.e 3 comes from = n-k+1), and then calculate the sum of three consecutive element of each row, the new matrix that you will get is 3X3. Now, find the maximum element in the matrix of dimension 3X3.
Example: matrix={{1, 1, 1, 1, 1} , {2, 2, 2, 2, 2}, {3, 8, 6, 7, 3} ,{4, 4, 4, 4, 4} ,{5, 5, 5, 5, 5}}
After calculating sum of three consecutive elements of each col, the new 5*3 matrix will be {{3,3,3},(6,6,6},{17,21,16},{12,12,12},{15,15,15}}

Then calculating the sum of three consecutive element of each row, the new matrix that you will get is 3X3. {{26, 30,25}, {35, 39,34}, {44, 48,43}}. Maximum element in this matrix is 48 which is the answer. In this way each number in the 3x3 matrix represents the sum of k*k elements.
"""
def Maximum_Sum(self, mat, n, k):
    # Your code goes here
    pre = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            if j == 0:
                pre[i][j] = mat[i][j]
            elif j < k:
                pre[i][j] = mat[i][j] + pre[i][j-1]
            else:
                pre[i][j] = mat[i][j] + pre[i][j-1] - mat[i][j-k]
    new = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = pre[i][j]
    for i in range(1,n):
        for j in range(k-1,n):
            if i < k:
                pre[i][j] = pre[i][j] + pre[i-1][j]
            else:
                pre[i][j] = pre[i][j] + pre[i-1][j] - new[i-k][j]
        #print(pre[i],new[i])
    ans = -float('inf')
    for i in range(k-1,n):
        #print(pre[i])
        for j in range(k-1,n):
            if pre[i][j] > ans:
                ans = pre[i][j]
    return ans