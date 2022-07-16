class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        mod = 10 **9 + 7
        
        for _ in range(maxMove):
            dp = [[(r== 0 or dp[r-1][c]) + (c==0 or dp[r][c-1]) + (r== m-1 or dp[r+1][c]) + (c== n-1 or dp[r][c+1]) for c in range(n)] for r in range(m) ]
        
        return dp[startRow][startColumn] % mod
        