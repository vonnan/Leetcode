class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = prices[0]
        res = 0
        for price in prices[1:]:
            if price > min_sofar:
                res = max(res, price - min_sofar)
            else:
                min_sofar = price
        return res
            