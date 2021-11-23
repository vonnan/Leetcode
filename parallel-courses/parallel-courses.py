class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        degree = [0] * n
        for u, v in relations:
            graph[u-1].add(v-1)
            degree[v-1] += 1
           
        q = deque([u for u in range(n) if degree[u] == 0])
        if not q:
            return -1
        seen = set([])
        n -= len(q)
        res = 0
        while q:
            m = len(q)
            for _ in range(m):
                u = q.popleft()
                seen.add(u)
                for v in graph[u]:
                    if v in seen:
                        return -1
                    if degree[v]:
                        degree[v] -= 1
                        if not degree[v]:
                            q.append(v)
                            n-=1
            res += 1
            
        return -1 if n else res
        
        