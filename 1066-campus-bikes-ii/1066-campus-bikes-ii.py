from heapq import heappush
from heapq import heappop

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        row, col = len(workers), len(bikes)
        
        dist = [[0] * col for _ in range(row)]
        for r in range(row):
            x_w, y_w = workers[r]
            for c in range(col):
                x_b, y_b = bikes[c]
                dist[r][c] = abs(x_w - x_b) + abs(y_w - y_b)
        
        heap = [(0, 0, 0)]
        
        seen = set([])
        
        while heap:
            cost, worker,  state = heappop(heap)
            if (worker, state) in seen:
                continue
            seen.add((worker, state))
            if worker == row:
                return cost
            
            for c in range(col):
                if state & (1 <<c) == 0:
                    w = dist[worker][c]
                    heappush(heap, (cost + w, worker + 1, state|(1<<c)))
            
                    
        