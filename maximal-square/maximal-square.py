class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        matrix = [[int(row[c]) for c in range(col)] for row in matrix]
        dp = [[0] * col for _ in range(row)]
        
        dp[0] = matrix[0][:]
        res = max(dp[0])
        for r in range(row):
            dp[r][0] = matrix[r][0]
            res = max(res, dp[r][0])
        
        
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]:
                    dp[r][c] = min(dp[r-1][c-1], dp[r][c-1], dp[r-1][c]) + 1
                    res = max(res, dp[r][c])
        
                    
        return res * res
        
        