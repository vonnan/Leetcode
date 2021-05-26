class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        row, col =   len(workers), len(bikes)
        dist = [[0]* col for r in range(row)]

        for r in range(row):
            wx, wy = workers[r]
            for c in range(col):
                bx, by = bikes[c]
                dist[r][c] = abs(wx-bx) + abs(wy-by)
                
        heap =[(0,0,0)]
        seen = set()
        
        while heap:
            cost, worker, taken_state = heappop(heap)
            
            if (worker, taken_state) in seen:
                continue
                
            seen.add(((worker, taken_state)))
            
            if worker == row:
                return cost
            
            for c in range(col):
                if taken_state & (1<<c) ==0:
                    w = dist[worker][c] 
                    new_taken_state = taken_state | 1<<c
                    heappush(heap, (cost + w, worker +1, new_taken_state))
                
        
            
            
                
                
                