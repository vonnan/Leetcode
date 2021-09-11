class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, sell, rest =[0]*n, [0]* n, [0]*n
        hold[0] = -prices[0]
        
        for i in range(1,n):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i-1], sell[i-1])
        
        return max(hold[-1], sell[-1], rest[-1])