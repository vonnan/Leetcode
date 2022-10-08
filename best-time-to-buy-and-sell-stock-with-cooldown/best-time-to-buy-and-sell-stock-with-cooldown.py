class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell, hold, rest = [0]*n, [0]*n, [0]*n
        hold[0] = -prices[0]
        
        for i, price in enumerate(prices[1:], 1):
            sell[i] = hold[i-1] + price
            rest[i] = max(sell[i-1], rest[i-1])
            hold[i] = max(rest[i-1] - price, hold[i-1])
            
        return max(rest[-1], sell[-1])
    