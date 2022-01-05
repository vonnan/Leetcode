class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(n)}
        graph = defaultdict(set)
        for u, v in A:
            indegree[u] += 1
            graph[v].add(u)
        
        q = [i for i, val in indegree.items() if val == 0 ]
        
        for v in q:
            for u in graph[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    q.append(u)
        
        return q if len(q) == n else []
        
        