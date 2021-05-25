from heapq import heappush
from heapq import heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        graph = defaultdict(list)
        for i, e in enumerate(edges):
            u,v = e
            p = succProb[i]
            graph[u].append((v,p))
            graph[v].append((u,p))
        
        if (start not in graph) or (end not in graph):
            return 0
        
        heap = [(1,start)]
        path = {i: inf for i in range(n)}
        #path[start] = 1
        
        while heap:
            cost, u = heappop(heap)
            if path[u] != inf:
                continue
                
            path[u] = cost
            if u == end:
                return 1/cost
            
            for v, p in graph[u]:
                if cost/p < path[v]:
                    heappush(heap, (cost/p,v))
        
        return 0
        