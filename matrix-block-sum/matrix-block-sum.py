class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        dp =[[0] * (col +1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                dp[r+1][c+1] = mat[r][c] + dp[r+1][c] + dp[r][c+1] - dp[r][c]
        
        for r in range(row):
            for c in range(col):
                lr, lc = max(r- K, 0), max(c-K, 0)
                rr, rc = min(r + K, row -1), min(c + K, col - 1)
                mat[r][c] = dp[rr+1][rc+1] + dp[lr][lc] - dp[rr+1][lc] - dp[lr][rc+1]
        
        return mat
        
        
        
  