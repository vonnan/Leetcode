from heapq import heappush
from heapq import heappop
from collections import defaultdict

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        dist =[[inf] * col for r in range(row)]
        dist[0][0] = 0
        visited = set()
        heap = [(0,0,0)]
        
        while heap:
            effort, r,c = heappop(heap)
            
            if (r,c) in visited:
                continue
                
            visited.add((r,c))
            
            for dr, dc in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr in range(row) and nc in range(col):
                    if (nr, nc) in visited:
                        continue
                    
                    eft = max(abs(heights[nr][nc] - heights[r][c]), effort)
                    if eft < dist[nr][nc]:
                        dist[nr][nc] = eft
                        heappush(heap, (eft, nr, nc))
                    
        return dist[-1][-1]
                    
            

        
        
                    
                
                
                
            