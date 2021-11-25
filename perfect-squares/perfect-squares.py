class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i* i for i in range(int(n **0.5), 0, -1)]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for amt in range(1, n+ 1):
            for num in nums:
                if num <= amt:
                    dp[amt] = min(dp[amt], dp[amt - num] + 1)
        return dp[-1]
            