class Solution:
    def canFinish(self, n: int, A: List[List[int]]) -> bool:
        graph = defaultdict(set)
        degree = [0] * n
        for u, v in A:
            graph[v].add(u)
            degree[u] += 1
            
        q = [v for v in range(n) if degree[v] == 0]
        for v in q:
            for u in graph[v]:
                degree[u] -= 1
                if degree[u] ==0:
                    q.append(u)
        return True if len(q) == n else False
                    