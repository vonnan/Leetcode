class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        empty = 1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    x,y = r, c
                elif grid[r][c] == 0:
                    empty += 1
        
        self.res = 0
        def dfs(r,c, empty):
            if not (0 <= r < row and 0 <= c < col and grid[r][c] >=0):
                return
            
            if grid[r][c] ==2:
                self.res += (empty == 0)
                return
                
            grid[r][c] -= 2
            dfs(r + 1, c, empty - 1)
            dfs(r - 1, c, empty - 1)
            dfs(r, c + 1, empty - 1)
            dfs(r, c - 1, empty - 1)
            grid[r][c] = 0
            
        dfs(x, y, empty)
        return self.res
                
        