class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        sets = set(range(n))
        
        while len(sets) > 2:
            leaves = set(u for u in sets if len(graph[u])==1)
            sets -= leaves
            for u in leaves:
                for v in graph[u]:
                    graph[v].remove(u)
        return sets
                
            