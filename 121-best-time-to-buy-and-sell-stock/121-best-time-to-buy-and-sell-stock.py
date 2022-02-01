class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        res = 0
        for i, p in enumerate(prices[1:], 1):
            if p > min_:
                res = max(p-min_, res)
            else:
                min_ = p
        return res