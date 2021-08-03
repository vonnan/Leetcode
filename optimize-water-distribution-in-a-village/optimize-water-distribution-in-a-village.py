from heapq import heappush
from heapq import heappop

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u,v,cost in pipes:
            graph[u][v] = graph[v][u] = min(graph[u].get(v, inf), cost)
        
        visited = set()
        res = 0
        heap = sorted([(cost, i) for i, cost in enumerate(wells, 1)])
        
        while heap:
            cost, i = heappop(heap)
            if i not in visited:
                visited.add(i)
                res += cost
                if len(visited) == n:
                    return res
                for j,c in graph[i].items():
                    heappush(heap, (c, j))
        return res
        
        