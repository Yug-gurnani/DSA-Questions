"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications. The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Example 1:

Input: N = 5
arr = {40, 20, 30, 10, 30}
Output: 26000
Explaination: There are 4 matrices of dimension 
40x20, 20x30, 30x10, 10x30. Say the matrices are 
named as A, B, C, D. The efficient way is 
(A*(B*C))*D. The number of operations are 20*30*10 
+ 40*20*10 + 40*10*30 = 26000.

So all we have to do is to bind the differnet matrix in different paranthesis
"""
def matrixMultiplication(self, n, arr):
    def solve(arr,i,j,mn,dp):
        if i >= j:# Base condition
            return 0
        if dp[i][j] != -1: #To avoid subproblems
            return dp[i][j]
        for k in range(i,j): # To check for all possible paranthesis
            dp[i][j] = solve(arr,i,k,mn,dp)+solve(arr,k+1,j,mn,dp)+(arr[i-1]*arr[k] * arr[j]) #To calculate cost
            if dp[i][j] < mn:# To calculate min. cost
                mn = dp[i][j]
        return mn
    dp = [[-1 for i in range(1001)]for i in range(1001)]
    
    mn = float('inf')
    return solve(arr,1,n-1,mn,dp)