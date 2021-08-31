class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        path = [(0,1),(0, -1), (1, 0), (-1, 0)]
        row, col = len(grid), len(grid[0])
        
        def dfs(r,c):
            if grid[r][c] == "1":
                grid[r][c] = "0"
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1":
                        dfs(nr, nc)
                return 1
            return 0
        
        res = 0
        for r in range(row):
            for c in range(col):
                res += dfs(r, c)
        return res