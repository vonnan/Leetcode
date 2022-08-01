class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        P, A = set([]), set([])
        
        row, col = len(heights), len(heights[0])
        
        P = set([(r,c) for r in range(row) for c in range(col) if r == 0 or c == 0])
        A= set([(r,c)  for r in range(row) for c in range(col) if r == row - 1 or c == col -1])
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        
        def helper(P):
            q = deque(list(P))
            visited = P
        
            while q:
                m = len(q)
                for _ in range(m):
                    r, c = q.popleft()
                    for dr, dc in path:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            P.add((nr, nc))
                
        
        helper(P)
        helper(A)
        
        return P & A
        
            