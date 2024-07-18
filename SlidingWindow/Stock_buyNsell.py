class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        max_sell = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            if prices[i] > max_sell:
                max_sell =prices[i]
            
            elif    prices[i] < max_sell:
                max_profit = max(max_profit,max_sell-prices[i])
        return max_profit