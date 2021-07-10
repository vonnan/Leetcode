from heapq import heappop
from heapq import heappush

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], A: List[int]) -> int:
        
        graph = defaultdict(list)
        
        for u,v,t in edges:
            graph[u].append((v,t))
            graph[v].append((u, t))
      
        n = len(A)
        
        passtime = {}
        
        heap = [(A[0], 0, 0)]
        while heap:
            cost, time, node = heappop(heap)
            if node == n-1:
                return cost
            
            if node not in passtime or passtime[node] > time:
                passtime[node] = time
                for v, t in graph[node]:
                    if time + t <= maxTime:
                        heappush(heap, (cost + A[v], time + t, v))
            
                
        return -1
            
            
            