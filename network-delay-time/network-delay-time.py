from heapq import heappush
from heapq import heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = defaultdict(dict)
        for u,v, t in times:
            dist[u][v] = t
            
        heap = [(0, k)]
        
        visited = set()
        
        while heap:
            t, u = heappop(heap)
            if u in visited:
                continue
            else:
                visited.add(u)
                if len(visited) == n:
                    return t
                for v, dt in dist[u].items():
                    if v not in visited:
                        heappush(heap, (t + dt, v))
        return -1
     