class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        coins = sorted([coin  for coin in coins if coin <= amount])
        for coin in coins:
            for amt in range(coin, amount +1):
                dp[amt] += dp[amt - coin]
        return dp[-1]        
                