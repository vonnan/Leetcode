class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row, col = len(grid), len(grid[0])
        
        keys = [0] * 6
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "@":
                    start = (r, c)
                elif grid[r][c].islower():
                    keys[ord(grid[r][c]) - ord("a")] = 1
        
        visited = set([(start[0], start[1],  "0"*6)])
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        q = deque([(start[0], start[1],  "0"*6)])
        keys = "".join(map(str,keys))
        
        res = 0
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                r,c,k = q.popleft()
                
                for dr,dc in path:
                    nr, nc = r + dr, c + dc
                    
                    
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != "#":
                        entry  = grid[nr][nc]
                        
                        if entry == "." or entry =="@":
                            if (nr, nc, k) not in visited:
                                q.append((nr,nc, k))
                                visited.add((nr, nc, k))
                                
                        elif entry.islower():
                            idx = ord(entry) - ord("a")
                            
                            
                            nk = k[:idx] + "1" + k[idx+1:]
                            if nk == keys:
                                return res
                            if (nr, nc, nk) not in visited:
                                q.append((nr,nc,nk))
                                visited.add((nr,nc,nk))
                        else:
                            idx = ord(entry) - ord("A")
                            if k[idx] == "1":
                                if (nr,nc,k) not in visited:
                                    q.append((nr, nc, k))
                                    visited.add((nr, nc, k))
        return -1
                            
            
        