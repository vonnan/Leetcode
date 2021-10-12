class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        path = [(0,1), (1,0), (0, -1), (-1, 0)]
        q, to_change = deque([]), set([])
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r,c,0))
                else:
                    to_change.add((r,c))
        
        while q:
            m = len(q)
            for _ in range(m):
                r,c,val = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in to_change:
                        mat[nr][nc] = val + 1
                        to_change.remove((nr, nc))
                        q.append((nr, nc, val + 1))
                        if not to_change:
                            return mat
        return mat
        
                