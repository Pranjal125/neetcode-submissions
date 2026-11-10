class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        max_profit =0
        for price in prices:
            total = price - left_min
            max_profit = max(max_profit,total)
            left_min = min(left_min,price)
        return max_profit
        