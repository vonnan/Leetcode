class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[0] * i for i in range(1, n + 1)]
        dp[0][0] = A[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + A[i][0]
            dp[i][i] = dp[i-1][i-1] + A[i][i]
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + A[i][j]
        return min(dp[-1])