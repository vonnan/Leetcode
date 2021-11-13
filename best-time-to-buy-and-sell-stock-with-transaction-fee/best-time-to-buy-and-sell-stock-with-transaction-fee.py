class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        rest, hold, sell = [0] * n, [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            
            rest[i] = max(rest[i-1], sell[i-1])
            hold[i] = max(hold[i-1], rest[i] - prices[i])
            sell[i] = hold[i-1] + prices[i] - fee
        
        return max(rest[-1], sell[-1])