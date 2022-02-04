class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        dp = [[0] * (n+1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        
        for g,p in zip(group, profit):
            for x in range(minProfit, -1, -1):
                for y in range(n-g, -1, -1):
                    dp[min(x + p, minProfit)][g + y] += dp[x][y]
        
        return sum(dp[-1]) % (10**9 + 7)