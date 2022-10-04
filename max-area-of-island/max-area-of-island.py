class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
            return 0
        
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    res = max(res, dfs(r, c))
        
        return res
                