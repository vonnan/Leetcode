from heapq import heappush
from heapq import heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        path = ((-1,0), (1,0), (0,-1), (0, 1))
        row, col = len(heights), len(heights[0])
        heap =[(0,0,0)]
        visited = set()
        
        while heap:
            effort, r, c = heappop(heap)
            if (r,c) in visited:
                continue
            if r== row-1 and c == col -1:
                return effort
            visited.add((r,c))
            
            for dr,dc in path:
                nr, nc = r+dr, c +dc
                if (nr, nc) in visited:
                    continue
                if 0<=nr<row and 0<=nc<col:
                    eft = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    
                    heappush(heap, (eft, nr, nc))
                        
        