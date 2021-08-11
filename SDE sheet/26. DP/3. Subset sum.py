"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination: 
The two parts are {1, 5, 5} and {11}.
"""
def equalPartition(self, n, arr):
    # code here
    s = sum(arr)
    if s%2 != 0:
        return 0
    else:
        target = s//2
        dp = [[False for i in range(target + 1)]for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(target+1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                else:
                    if j >= arr[i-1]:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
        return int(dp[n][target])
"""
TC = o(n*s)
SC = o(n*s)
"""
        