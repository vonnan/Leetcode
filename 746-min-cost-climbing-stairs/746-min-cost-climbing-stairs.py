class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp =[0] * 2 + [inf] * (len(cost)-1)
        for i in range(len(cost)-1):
            dp[i+2] = min(dp[i] + cost[i], dp[i+1] + cost[i+1])
        return dp[-1]
            