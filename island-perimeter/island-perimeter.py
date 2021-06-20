class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = set()
        path = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i in range(row):
            for j in range(col):
                if grid[i][j]== 1:
                    islands.add((i,j))
        
        res = 0
        for x in range(row):
            for y in range(col):
                if (x,y) in islands:
                    res += 4
                    for dx, dy in path:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in islands:
                            res -= 1
        
        return res
                    