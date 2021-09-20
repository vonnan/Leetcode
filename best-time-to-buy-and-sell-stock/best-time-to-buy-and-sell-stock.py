class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar = inf
        res = 0
        for p in prices:
            if p > min_sofar:
                res = max(res, p - min_sofar)
            min_sofar = min(min_sofar, p)
        return res