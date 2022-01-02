class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        
        for u, v in edges:
            graph[u].add(v)
        
        seen = set([])
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei == node or nei in seen or not dfs(nei):
                    return False
            seen.discard(node) 
            #print(graph[node], node==destination)
            return graph[node] or node == destination
        
        return dfs(source)