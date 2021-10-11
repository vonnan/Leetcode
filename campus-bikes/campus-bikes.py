from heapq import heappush
from heapq import heappop
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist = []
        
        heap = []
        row, col = len(workers), len(bikes)
        for r in range(row):
            x, y = workers[r]
            tmp = []
            for c in range(col):
                xb, yb = bikes[c]
                d = abs(x- xb) + abs(y - yb)
                tmp.append((d, r, c))
            tmp.sort()
            heappush(heap, tmp.pop(0))
            dist.append(tmp)
        res =[inf] * row
        
        used = set([])
        
        
        while len(used) < row:
            d, r, c = heappop(heap)
            if c not in used:
                res[r] = c
                used.add(c)
                
            else:
                heappush(heap, dist[r].pop(0))
                
        return res
                
                
            
            
        