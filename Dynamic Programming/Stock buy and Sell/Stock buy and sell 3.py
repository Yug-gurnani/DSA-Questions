"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        
        dp = [[0 for i in range(n)] for i in range(3)]
        
        for i in range(1,3):
            maxdiff = -prices[0]
            for j in range(1,n):
                
                dp[i][j] = max(dp[i][j-1], prices[j] + maxdiff)
                
                maxdiff = max(maxdiff, dp[i-1][j] - prices[j])
        # print(dp)
        return dp[2][n-1]


