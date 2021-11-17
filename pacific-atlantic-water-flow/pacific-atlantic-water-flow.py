class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row, col = len(heights), len(heights[0])
        visited_p = set([])
        visited_a = set([])
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            
            visited.add((r, c))
            
            for dr,dc in path:
                nr, nc = r + dr, c + dc
                if 0<= nr< row and 0 <= nc < col and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)
        
        for r in range(row):
            dfs(r, 0, visited_p)
            dfs(r, col -1, visited_a)
        
        for c in range(col):
            dfs(0, c, visited_p)
            dfs(row -1, c, visited_a)
        
        return visited_p & visited_a
        
    
        
        