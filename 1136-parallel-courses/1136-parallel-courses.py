class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        in_degree = [0] * n
        
        for u, v in relations:
            graph[u- 1].add(v -1)
            in_degree[v - 1] += 1
        
        q = deque([v for v in range(n) if in_degree[v] == 0])
        if not q:
            return -1
        
        semester = 0
        seen = set(q)
        n -= len(q)
        while q:
            m = len(q)
            semester += 1
            for _ in range(m):
                u = q.popleft()
                seen.add(u)
                for v in graph[u]:
                    if v in seen:
                        return -1
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q.append(v)
                        seen.add(v)
                        n -= 1
        return -1 if n else semester
                    
                    
                    
        
        