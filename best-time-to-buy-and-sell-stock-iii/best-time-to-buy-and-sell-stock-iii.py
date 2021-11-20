class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_f = [0] * (n + 1)
        min_, max_ = prices[0], 0
        for i, price in enumerate(prices[1:], 2):
            if price > min_:
                if price- min_ > max_:
                    max_ = price - min_
            else:
                min_ = price
            dp_f[i] = max_
        dp_f = dp_f[1:]
        
        dp_b = [0] * (n + 1)
        max_, max_p = prices[-1], 0
        
        for i, price in enumerate(prices[::-1][1:], 2):
            
            if price < max_:
                if max_ - price > max_p:
                    max_p = max_ - price
            else:
                max_ = price
            dp_b[i] = max_p
        
        dp_b = dp_b[::-1][:-1]
        
        return max(dp_f[i] + dp_b[i] for i in range(n))
        
            