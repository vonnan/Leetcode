class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        land = [(r,c) for r in range(row) for c in range(col) if grid[r][c]]
        sets = set(land)
        
        res = 4 * len(land)
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        while land:
            r, c = land.pop()
            res -= sum((r+dr, c + dc) in sets for dr,dc in path)
        return res