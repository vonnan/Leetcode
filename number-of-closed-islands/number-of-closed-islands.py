class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == 0:
                grid[r][c] = 1
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
        
        sets = set([(r,c) for r in range(row) for c in range(col) if (r == 0 or r== row -1 or c==0 or c == col -1) and grid[r][c] == 0])
        
        for r,c in sets:
            dfs(r, c)
        
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    dfs(r, c)
                    res += 1
        
        return res