class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        
        coins.sort()
        
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        
        return dp[-1]