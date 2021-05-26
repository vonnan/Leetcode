from heapq import heappush
from heapq import heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v, w))
            
        heap =[(0, k)]
        dist = {i: inf for i in range(1, n+1)}
        visited = set([])
        
        while heap:
            cost, u = heappop(heap)
            if u in visited:
                continue
                
            visited.add(u)
            dist[u] = cost
            if len(visited) ==n:
                return cost
            
            
            for nei, w in graph[u]:
                if nei in visited:
                    continue
                if cost + w < dist[nei]:
                    heappush(heap, (cost+w, nei))
                
        return -1
                
                
            
            