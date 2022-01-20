from heapq import heappush
from heapq import heappop

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        memo = set()
        heap = [(0, node, 1 << node) for node in range(n)]
        
        final = (1<<n) - 1
        
        while heap:
            step, node, state = heappop(heap)
            if state == final:
                return step 
            for v in graph[node]:
                nxt = state | (1 << v)
                if (nxt, v) not in memo:
                    memo.add((nxt, v))
                    heappush(heap, (step + 1, v, nxt))
            