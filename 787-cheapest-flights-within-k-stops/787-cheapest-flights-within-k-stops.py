from heapq import heappush
from heapq import heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nei = defaultdict(dict)
        for u, v, cost in flights:
            nei[u][v] = cost
       
        
        heap = [(0, 0, src)]
        seen = {src: 0}
        
        while heap:
            cost, stop, u = heappop(heap)
            seen[u] = stop
            if u == dst:
                return cost
            if stop == k + 1:
                continue
                
            for v in nei[u]:
                if v in seen and seen[v] <= stop + 1:
                    continue
                else:
                    heappush(heap, (cost + nei[u][v], stop + 1, v))
        
        return -1
                    
            
            