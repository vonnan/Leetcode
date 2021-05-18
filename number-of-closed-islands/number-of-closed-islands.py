class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col, res = len(grid), len(grid[0]), 0
        
        if not grid or not grid[0]:
            return 0
        
        def dfs(i,j):
            if 0<=i<row and 0<=j<col and grid[i][j] ==0:
                grid[i][j] = 1
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1,j)
                dfs(i, j-1)
                
        
        for i in range(row):
            for j in range(col):
                if i==0 or i == row-1 or j == 0 or j == col - 1 and grid[i][j]==0:
                    dfs(i,j)
        
       
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] ==0:
                    dfs(i,j)
                    res += 1
                
        return res
                
        
        