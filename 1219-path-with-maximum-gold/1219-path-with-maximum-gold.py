class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = set([])
        
        row, col = len(grid), len(grid[0])
        res = 0
        def dfs(r,c):
            if 0<= r < row and 0 <= c < col and grid[r][c] and not seen[r][c]:
                seen[r][c] = 1
                ans =  grid[r][c] + max(dfs(r + dr, c + dc) for dr, dc in path)
                seen[r][c] = 0
                return ans
            return 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    seen = [[0] * col for _ in range(row)]
                    res = max(res, dfs(r, c))
                
        return res
                
                