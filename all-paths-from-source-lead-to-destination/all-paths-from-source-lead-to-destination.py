class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei == node or nei in seen or not dfs(nei):
                    return False
            seen.discard(node)
            return graph[node] or node == destination
        
        seen = set()
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        return dfs(source)
            