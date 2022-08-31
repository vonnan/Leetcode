class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        
        P = set([(0, c) for c in range(col)]) | set([(r, 0) for r in range(row)])
        A = set([(row -1, c) for c in range(col)]) | set([(r, col -1) for r in range(row)])
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        q = deque(list(P))
        seen = P
        
        while q:
            r, c = q.popleft()
            #print(r,c, P)
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and ((nr, nc) not in seen) and heights[nr][nc] >= heights[r][c]:
                    q.append((nr, nc))
                    seen.add((nr, nc))
                    P.add((nr, nc))
        
        q = deque(list(A))
        seen = A
        
        while q:
            r, c = q.popleft()
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    q.append((nr, nc))
                    seen.add((nr, nc))
                    A.add((nr, nc))
        
        return P & A