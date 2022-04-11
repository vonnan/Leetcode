class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        lst = [(r,c) for r in range(row) for c in range(col) if grid[r][c]]
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and grid[r][c] and not seen[r][c]: 
                seen[r][c] = 1
                ans = grid[r][c] + max(dfs(r + 1, c), dfs(r-1,c), dfs(r, c+1), dfs(r, c-1))
                seen[r][c] = 0
                return ans
            return 0
        
        
        for r,c in lst:
            seen =[[0]*col for _ in range(row)]
            res = max(res, dfs(r,c))
        return res
        
            
            
        
        