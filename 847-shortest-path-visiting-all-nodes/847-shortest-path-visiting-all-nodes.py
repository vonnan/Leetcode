from heapq import heappush
from heapq import heappop
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final = (1 <<n) -1
        memo,heap= set(), [(0, node, 1 << node) for node in range(n)]
        
        while heap:
            step, node, state = heappop(heap)
            if state == final:
                return step
            for v in graph[node]:
                nxt = (1<<v) | state
                if (nxt, v) not in memo:
                    heappush(heap, (step + 1, v, nxt))
                    memo.add((nxt, v))
        
        
                
                
            
            