class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        n = len(A)
        dp = [[0] * i for i in range(1, n+1)]
        dp[0][0] = A[0][0]
        
        for r in range(1, n):
            dp[r][0] = dp[r-1][0] + A[r][0]
            dp[r][r] = dp[r-1][r-1] + A[r][r]
            
            for c in range(1, r):
                dp[r][c] = min(dp[r-1][c-1], dp[r-1][c]) + A[r][c]
        
        return min(dp[-1])
                