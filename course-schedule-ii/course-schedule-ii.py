class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        degree = [0] * n
        
        for u, v in A:
            degree[u] += 1
            graph[v].add(u)
            
        q = [v for v in range(n) if degree[v] == 0 ]
        
        for v in q:
            for u in graph[v]:
                degree[u] -= 1
                if degree[u] == 0:
                    q.append(u)
        
        return q if len(q) == n else []