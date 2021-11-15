class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        rest, hold, sell = [0] * n, [0] * n, [0] * n
        
        hold[0] = -prices[0]
        
        for i, price in enumerate(prices[1:], 1):
            sell[i] = hold[i-1] + price - fee
            rest[i] = max(rest[i-1], sell[i])
            hold[i] = max(hold[i-1], rest[i] - price)
        
        return max(rest[-1], sell[-1])