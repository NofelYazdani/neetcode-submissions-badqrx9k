class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = 0
        current = 0
        left = 0
        right = 0
        while right < len(prices):
            current = prices[right] - prices[left]
            if current <= 0:
                left = right
            else:
                best_price = max(current, best_price)
            right = right + 1

        return best_price




        