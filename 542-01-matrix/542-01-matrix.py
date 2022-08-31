class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        q = deque([])
        sets = set([])
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                else:
                    sets.add((r, c))
        
        if not sets:
            return mat
        
        while q:
            m = len(q)
            for _ in range(m):
                r,c,val = q.popleft()
            
                for dr,dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) in sets:
                        mat[nr][nc] = val + 1
                        sets.remove((nr, nc))
                        q.append((nr, nc, val + 1))
        
        return mat
                        
                    
                    