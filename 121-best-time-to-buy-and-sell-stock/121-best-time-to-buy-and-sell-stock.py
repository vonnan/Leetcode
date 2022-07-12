class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        res = 0
        for price in prices[1:]:
            if price < min_:
                min_ = price
            else:
                res = max(res, price - min_)
        return res