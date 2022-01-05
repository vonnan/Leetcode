from heapq import heappush
from heapq import heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, cost in flights:
            graph[u][v] = cost
        
        k += 1
        heap = [(0, 0, src)]
        
        seen = {src: 0}
        
        while heap:
            cost, stop, u = heappop(heap)
            seen[u] = stop
            
            if stop <= k:
                if u == dst:
                    return cost
                for v in graph[u]:
                    if v in seen and seen[v] <= stop + 1:
                        continue
                    heappush(heap, (graph[u][v] + cost, stop + 1, v))
        return -1