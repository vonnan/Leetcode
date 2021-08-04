class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        row, col = len(heights), len(heights[0])
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        seen_a, seen_p = set(), set()
        
        def dfs(r, c, seen):
            seen.add((r,c))
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)
                    
        # initialize
        
        for r in range(row):
            dfs(r, 0, seen_p)
            dfs(r, col -1, seen_a)
            
        for c in range(col):
            dfs(0, c, seen_p)
            dfs(row - 1, c, seen_a)
            
            
        return [(r,c) for r in range(row) for c in range(col) if (r,c) in seen_a and (r,c) in seen_p]
                    
                    