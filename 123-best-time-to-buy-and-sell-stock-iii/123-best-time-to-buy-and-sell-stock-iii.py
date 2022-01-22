class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        
        dp = [0] * n
        min_ = prices[0]
        for i, price in enumerate(prices[1:], 1):
            if price > min_:
                dp[i] = price - min_
            else:
                min_ = price
        
        dp_b = [0] * n
        max_ = prices[-1]
        for i in range(n-2, -1, -1):
            if prices[i] <= max_:
                dp_b[i] = max(dp_b[i+1], max_ - prices[i])
            else:
                max_ = prices[i]
                dp_b[i] = max(dp_b[i], dp_b[i+1])
        
        return max(dp[i] + dp_b[i] for i in range(n))
            
        