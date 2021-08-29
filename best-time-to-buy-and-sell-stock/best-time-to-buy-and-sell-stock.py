class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lst =sorted([(price, i) for i, price in enumerate(prices)])
        res = 0
        print(lst)
        for i, price in enumerate(prices):
            if price >= lst[-1][0]:
                continue
            while lst[-1][1] < i:
                lst.pop()
            
            res = max(res, lst[-1][0] - price)
        return res