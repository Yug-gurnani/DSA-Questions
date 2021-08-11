"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        n = len(arr)
        
        ans = 0
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                ans += arr[i] - arr[i-1]
                
        return ans