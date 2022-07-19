class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0
        for c in cost:
            prev, curr = curr, min(prev, curr) + c
        return min(prev, curr)
