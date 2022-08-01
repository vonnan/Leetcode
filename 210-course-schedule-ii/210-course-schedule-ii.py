class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree ={u: 0 for u in range(n)}
        
        for u, v in A:
            graph[v].add(u)
            indegree[u] += 1
            
        q = [u for u, val in indegree.items() if not val]
        
        for v in q:
            for u in graph[v]:
                indegree[u] -= 1
                if not indegree[u]:
                    q.append(u)
        
        return q if len(q) == n else []
        