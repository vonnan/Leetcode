from heapq import heappush
from heapq import heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = [(0, 0, src)]
        k += 1
        graph = defaultdict(set)

        for u,v,cost in flights:
            graph[u].add((v, cost))
            
        seen = {src: 0}
        
        while heap:
            cost, stop, node = heappop(heap)
            seen[node] = stop
            
            if stop <= k :
                if node == dst:
                    return cost
                for v, fare in graph[node]:
                    if v in seen and seen[v] <= stop + 1:
                        continue
                    
                    heappush(heap, (cost + fare, stop + 1, v))
                    
        return -1
                