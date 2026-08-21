
"""
LeetCode 121 - Best Time to Buy and Sell Stock

Difficulty: Easy
Topic: Arrays, Greedy

Problem Summary:
Given an array where each value represents the stock price on a
particular day, find the maximum profit possible by buying once
and selling once. The buy must happen before the sell.

Approach:
- Keep track of the minimum price seen so far.
- For each price, calculate the profit if we sell on that day.
- Keep track of the maximum profit found.

Time Complexity:
O(n)

Space Complexity:
O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == "__main__":
    obj = Solution()

    print(obj.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(obj.maxProfit([7, 6, 4, 3, 1]))      # 0
