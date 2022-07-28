from heapq import heappush
from heapq import heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = grid[0][0]
        n = len(grid)
        seen = set([(0, 0)])
        heap = [(grid[0][0], 0, 0)]
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        while True:
            t, r, c= heappop(heap)
            if r == n-1 and c == n-1:
                return max(res, t)
            
            res = max(res, t)
            seen.add((r,c))
            for dr,dc in path:
                nr, nc = r + dr, c + dc
                if 0<= nr <n and 0 <= nc < n and (nr, nc) not in seen:
                    heappush(heap, (grid[nr][nc], nr, nc))
        
            
            
            
            
            
