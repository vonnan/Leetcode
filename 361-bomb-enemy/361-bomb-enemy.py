class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        
        dp = [[0] * col for _ in range(row)]
        for r in range(row):
            ct = 0
            for c in range(col):
                val = grid[r][c]
                if val == "W": ct = 0
                elif val== "E": ct += 1
                else:
                    dp[r][c] = ct
                    
        for r in range(row):
            ct = 0
            for c in range(col -1, -1, -1):
                val = grid[r][c]
                if val == "W":
                    ct = 0
                if val == "E":
                    ct += 1
                else:
                    dp[r][c] += ct
        
        
        for c in range(col):
            ct = 0
            for r in range(row):
                val = grid[r][c]
                if val == "W":
                    ct = 0
                if val == "E":
                    ct += 1
                else:
                    dp[r][c] += ct
        
        for c in range(col):
            ct = 0
            for r in range(row-1, -1, -1):
                val = grid[r][c]
                if val == "W":
                    ct = 0
                if val == "E":
                    ct += 1
                else:
                    dp[r][c] += ct
                    
        return max([dp[r][c] for r in range(row) for c in range(col) if grid[r][c] == "0"] or [0])
            
            
