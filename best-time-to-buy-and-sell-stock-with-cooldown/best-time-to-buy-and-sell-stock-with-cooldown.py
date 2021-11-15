class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rest, hold, sell = [0] * n, [0] * n, [0] *n
        hold[0] = -prices[0]
        for i in range(1,n):
            rest[i] = max(rest[i-1], sell[i-1])
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sell[i] = hold[i-1] + prices[i]
        return max(sell[-1], rest[-1])
        