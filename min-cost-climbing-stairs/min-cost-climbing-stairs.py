class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0
        
        n = len(cost)
        
        for i in range(1, n):
            prev, curr = min(curr, prev+ cost[i-1]), min(curr + cost[i], prev+ cost[i-1])
        return curr