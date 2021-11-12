class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_ = prices[0]
        for price in prices[1:]:
            res = max(res, price - min_)
            min_ = min(min_, price)
        return res