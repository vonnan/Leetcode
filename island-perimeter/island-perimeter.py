class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        land = set([(r,c) for r in range(row) for c in range(col) if grid[r][c] == 1])
        sets = land.copy()
        res = 0
        while land:
            r,c = land.pop()
            res += 4 - sum((r+dx, c + dy) in sets for dx,dy in ((-1,0), (1,0),(0,1),(0,-1)))
            
        return res
            