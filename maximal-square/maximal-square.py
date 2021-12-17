class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        
        dp =[[0]* (col + 1) for _ in range(row + 1)]
        
        
        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    dp[r+1][c+1] = int(matrix[r][c])
        
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == "1":
                    dp[r+1][c+1] = max(dp[r+1][c+1], min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1)
                   
                    
        return max([max(rows) for rows in dp])**2
                    