class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        current_minimum = prices[0]
        for i in range(1, len(prices)):
            current_profit = prices[i] - current_minimum 
            if current_profit > max_profit:
                max_profit = current_profit 
            if prices[i] < current_minimum:
                current_minimum = prices[i]
        return max_profit 