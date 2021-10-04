class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        for r in range(row):
            rows = grid[r]
            for c in range(col):
                if grid[r][c] != "0":
                    continue
                
                ct = 0
                
                #count left
                
                left = c-1
                
                while left >= 0 and rows[left] != "W":
                    
                    if rows[left] == "E":
                        ct += 1
                        
                    left -= 1
                
                right = c + 1
                while right < col and rows[right] != "W":
                    if rows[right] == "E":
                        ct += 1
                    right += 1
                    
                up = r -1
                while up >= 0 and grid[up][c] != "W":
                    if grid[up][c] == "E":
                        ct += 1
                    up -= 1
                
                down = r + 1
                while down < row and grid[down][c] != "W":
                    if grid[down][c] == "E":
                        ct += 1
                    down += 1
                   
                res = max(res, ct)
                
        return res