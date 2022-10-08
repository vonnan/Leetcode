class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            matrix[r] = [inf] + matrix[r] + [inf]
        
        dp = [inf] + [0] * col + [inf]
        
        for rows in matrix:
            dp2 =  [inf] + [0] * col + [inf]
            for c in range(1, col + 1):
                dp2[c] = rows[c] + min(dp[c-1], dp[c], dp[c+1])
            dp = dp2
        return min(dp)