class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dp = [[0] * col for _ in range(row)]
        
        def helper(r, c):
            if dp[r][c]:
                return dp[r][c]
            
            res = 1
            
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, helper(nr, nc) + 1)
            
            dp[r][c] = res
            return res
        
        return max(helper(r,c) for r in range(row) for c in range(col))
            
            