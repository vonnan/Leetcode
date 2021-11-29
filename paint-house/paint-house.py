class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        row, col = len(costs), len(costs[0])
        dp = [[0] * col for _ in range(row)]
        dp[0] = costs[0]
        for r , rows in enumerate(costs[1:], 1):
            for c in range(col):
                dp[r][c] = min(dp[r-1][:c] + dp[r-1][c+1:]) + costs[r][c]
        return min(dp[-1])