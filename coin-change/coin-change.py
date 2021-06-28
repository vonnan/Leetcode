class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ways = [inf] * (amount + 1)
        ways[0] = 0
        coins.sort()
        
        for amt in range(1, amount + 1):
            for coin in coins:
                if coin <= amt:
                    ways[amt] = min(ways[amt], ways[amt - coin] + 1)
        
        return ways[-1] if ways[-1] != inf else -1