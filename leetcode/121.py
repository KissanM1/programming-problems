"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Solution Runtime: 24ms
Beats 92.25%
"""



import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = sys.maxsize
        for price in prices:
            if (price < lowest):
                lowest = price
            if (price - lowest > maxProfit):
               maxProfit =  price - lowest

        return maxProfit
            