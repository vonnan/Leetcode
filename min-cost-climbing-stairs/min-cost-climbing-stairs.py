class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(1, n):
            
            dp[i+ 1] = min(dp[i] + cost[i], dp[i-1] + cost[i-1])
        
        return dp[-1]