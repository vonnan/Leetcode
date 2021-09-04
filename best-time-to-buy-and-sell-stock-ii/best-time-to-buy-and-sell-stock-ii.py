class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy  = prices[0]
        res, n = 0, len(prices)
        for i, price in enumerate(prices[1:], 1): 
            if i == len(prices) -1:
                if price > buy:
                    return res + price - buy
            if price <= buy:
                buy = price
            else:
                res += price - buy
                buy = price
        return res
        
            
            
            