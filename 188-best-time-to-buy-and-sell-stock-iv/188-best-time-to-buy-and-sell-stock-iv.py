class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n//2:
            return sum(prices[i] - prices[i-1] for i in range(1, n) if prices[i] > prices[i-1])
        
        dp = [[0] * n for _ in range(k+1)]
        
        for r in range(1, k + 1):
            buy = -prices[0]
            for c in range(1, n):
                dp[r][c] = max(dp[r][c], dp[r][c-1], prices[c] + buy)
                buy = max(buy, dp[r-1][c-1] - prices[c])
        
        return dp[-1][-1]