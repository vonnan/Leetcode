class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        
        dp[0], dp[1] = cost[0], cost[1]
        
        cost += [0]
        for i in range(2,n + 1):
            dp[i] = min(dp[i-2] , dp[i-1]) + cost[i]
        return dp[-1]