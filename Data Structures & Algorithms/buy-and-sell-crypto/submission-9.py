class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = len(prices) - 2
        right = len(prices) - 1

        while left >= 0:
            if prices[left] > prices[right]:
                right = left     # update max selling price
            else:
                profit = max(profit, prices[right] - prices[left])
            
            left -= 1

        return profit