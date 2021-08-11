"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
 Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def solve(arr,n):
    minele = float('inf')
    profit = 0
    for i in range(n):
        minele = min(minele,arr[i])
        profit = max(profit,arr[i] - minele)
    return profit
#TC = o(n)
#SC = o(1)
