class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and grid[r][c]:
                grid[r][c] = 0
                return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            return 0
        
        return max(dfs(r,c) for r in range(row) for c in range(col))
            