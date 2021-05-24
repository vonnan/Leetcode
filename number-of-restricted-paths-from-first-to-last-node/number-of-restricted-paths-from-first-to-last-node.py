import collections
import functools
import heapq
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        @functools.cache
        def dfs(node: int) -> int:
            if node == 1: return 1
            result = 0
            for nei in graph[node]:
                if dist[nei] > dist[node]:
                    result = (result + dfs(nei)) % mod
            return result

        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        dist, heap, mod = {n: 0}, [(0, n)], 10**9 + 7
        while heap:
            shortest, node = heapq.heappop(heap)
            if shortest != dist[node]: continue
            for nei, w in graph[node].items():
                if dist[node] + w < dist.get(nei, float('inf')):
                    dist[nei] = dist[node] + w
                    heapq.heappush(heap, (dist[nei], nei))
        return dfs(n)
                    
                
                    
            