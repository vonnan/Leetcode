class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [inf] * (amount + 1)
        dp[0] = 0
        
        for amt in range(1, amount + 1):
            for coin in coins[::-1]:
                if coin == amt:
                    dp[amt] = 1
                elif coin < amt:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        return dp[-1] if dp[-1] != inf else -1
                