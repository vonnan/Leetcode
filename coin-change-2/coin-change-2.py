class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            if coin > amount:
                break
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        return dp[-1]
        