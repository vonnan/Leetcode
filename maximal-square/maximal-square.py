class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        
        dp=[[0] * (col + 1) for _ in range(row + 1)]
        res = -inf
        for r in range(row):
            for c in range(col):
                if matrix[r][c] =="1":
                    dp[r+ 1][c + 1] = min([dp[r + 1][c], dp[r][c+ 1], dp[r][c]]) + 1
                    res = max(res, dp[r+1][c+1])
                
        return res * res if res != -inf else 0
        