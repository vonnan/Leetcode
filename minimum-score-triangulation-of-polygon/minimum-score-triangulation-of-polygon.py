class Solution:
    
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range( n- d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[j] * values[k] for k in range(i+1, j))
        return dp[0][n-1]