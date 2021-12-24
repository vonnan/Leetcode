class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        row, col = len(costs), len(costs[0])
        
        dp = costs[0]
        
        for cost in costs[1:]:
            
            dp = [cost[c] + min(dp[:c] + dp[c+1:]) for c in range(col)]
            
        return min(dp)
                