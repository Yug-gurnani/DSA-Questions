"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
class Solution:
    def maxProfit(self, k, arr):
        n = len(arr)
        if k >= n:
            ans = 0
            for i in range(1,n):
                if arr[i] > arr[i-1]:
                    ans += arr[i] - arr[i-1]
                    
            return ans
        
        else:
            
            dp = [[0 for i in range(n)]for i in range(k+1)]
            
            for i in range(1,k+1):
                maxdiff = -arr[0]
                for j in range(1,n):
                    dp[i][j] = max(dp[i][j-1], arr[j] + maxdiff)
                    
                    maxdiff = max(maxdiff, dp[i-1][j] - arr[j])
                    
            
            return dp[k][n-1]
                    