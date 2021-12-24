class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        row, col = len(costs), len(costs[0])
        
        dp = costs[0]
        for i, cost in enumerate(costs[1:], 1):
            dp = [cost[c] + min(dp[:c] + dp[c+1:]) for c in range(3)]
            
        
        return min(dp)     