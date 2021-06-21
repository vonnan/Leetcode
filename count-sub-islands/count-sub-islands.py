class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        path = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(grid1), len(grid1[0])
        
        def dfs(r,c):
            if not (0 <= r < row and 0 <= c < col and grid2[r][c] ==1):
                return 1
            
            grid2[r][c] = 0
            
            res = grid1[r][c]
            
            for dr, dc in path:
                res &= dfs(r + dr, c + dc)
                
            return res
        
        return sum(dfs(r,c) for r in range(row) for c in range(col) if grid2[r][c])
            
            
                
                
                