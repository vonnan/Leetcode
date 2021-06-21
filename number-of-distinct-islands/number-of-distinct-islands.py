class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        land = set()
        self.step = ""
        
        def dfs(r,c, direction):
            if 0 <= r < row and 0 <= c <col and grid[r][c]==1:
                grid[r][c] = 0
                self.step += direction
                dfs(r-1, c, "U")
                dfs(r+1, c, "D")
                dfs(r, c-1, "L")
                dfs(r, c+1, "R")
                self.step += "B"
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1:
                    dfs(r,c,"O")
                    land.add(self.step)
                    self.step = ""
        
        return len(land)
                