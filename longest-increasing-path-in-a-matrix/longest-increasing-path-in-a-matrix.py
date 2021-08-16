class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        
        if row == 0 or col ==0:
            return 0
        
        dp = [[0]*col for _ in range(row)]
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r,c):
            if dp[r][c] > 1:
                return dp[r][c]
            
            res = 1
            
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if dp[nr][nc] < dp[r][c]:
                        continue
                    if matrix[nr][nc] > matrix[r][c]:
                        res = max(res, dfs(nr, nc) + 1)
                        
            dp[r][c] = res
            
            return res
        
        return max(dfs(r,c) for c in range(col) for r in range(row))
                    
            
            
