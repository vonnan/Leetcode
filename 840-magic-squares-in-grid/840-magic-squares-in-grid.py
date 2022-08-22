class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        sets = set(list(range(1, 10)))
        row, col = len(grid), len(grid[0])
        if row < 3 or col < 3:
            return 0
        
        for r in range(1, row -1):
            for c in range(1, col -1):
                if grid[r][c] == 5:
                    if set([ grid[x][y] for x in range(r-1, r + 2) for y in range(c-1, c + 2)]) == sets and all(grid[x][c-1] + grid[x][c] + grid[x][c + 1] == 15 for x in range(r-1, r + 2)) and all((grid[r-1][y] + grid[r][y] + grid[r+1][y] )== 15 for y in range(c-1, c +2)) and (grid[r-1][c-1] + grid[r+1][c+1] == grid[r+1][c-1] + grid[r-1][c+1] == 10):
                        res += 1
        
        return res
                        
                            