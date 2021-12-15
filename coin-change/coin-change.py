class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = 1)
        
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for amt in range(1, amount + 1):
            for coin in coins:
                if coin  > amt:
                    continue
                else:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        
        return dp[-1] if dp[-1] != inf else -1
            