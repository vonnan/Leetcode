class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        
        path = [(0,1), (1,0), (-1,0), (0,-1)]
        dp = [[0] * col for _ in range(row)]
        
        def dfs(r,c):
            if dp[r][c] > 1:
                return dp[r][c]
            res = 1
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if A[nr][nc] > A[r][c]:
                        res = max(res, dfs(nr, nc) + 1)
            dp[r][c] = res
            return res
        
        return max(dfs(r,c) for r in range(row) for c in range(col))
                