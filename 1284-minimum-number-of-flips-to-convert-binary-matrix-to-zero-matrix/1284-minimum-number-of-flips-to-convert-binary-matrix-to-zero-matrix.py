class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        
        tot = row * col
        
        path = [(0,1), (1,0), (0, -1), (-1, 0)]
        res = inf
        for mask in range(1 << tot):
            new = [ rows[:] for rows in mat]
            ct = 0
            for i in range(tot):
                if mask & (1<<i):
                    r, c = divmod(i, col)
                    ct += 1
                    new[r][c] = 1- new[r][c]
                    for dr, dc in path:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < row and 0 <= nc < col:
                            new[nr][nc] = 1 - new[nr][nc]
                
            if sum(rows.count(1) for rows in new) == 0:
                res = min(res, ct)
        
        return res if res != inf else -1
                            
                
            
            