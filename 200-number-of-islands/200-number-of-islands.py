class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r - 1, c)
                return 1
            return 0
        
       
        return sum(dfs(r, c) for r in range(row) for c in range(col))