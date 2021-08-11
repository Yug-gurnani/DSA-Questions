"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minele = prices[0]
        
        for i in range(len(prices)):
            if prices[i] <= minele:
                minele = prices[i]
            else:
                profit = max(profit, prices[i] - minele)
                
        return profit