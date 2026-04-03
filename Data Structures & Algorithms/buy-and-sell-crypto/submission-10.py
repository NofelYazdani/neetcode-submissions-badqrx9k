class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = len(prices) - 2, len(prices) -1

        while left >= 0:
            if (prices[right] - prices[left]) >= 0:
                profit = max(profit,prices[right] - prices[left])
                left = left - 1
            else:
                right = left
                left = left - 1
        return profit 

        