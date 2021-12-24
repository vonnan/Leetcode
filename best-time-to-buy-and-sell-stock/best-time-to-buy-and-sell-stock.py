class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        
        res = 0
        
        for price in prices[1:]:
            res = max(price - min_, res)
            min_ = min(min_, price)
        return res