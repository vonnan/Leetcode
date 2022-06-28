class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        n = len(edges) + 1
        
        q = deque([0])
        
        level = 0
        
        visited = set([0])
        
        while q:
            m = len(q)
            last = list(q)
            level += 1
            for _ in range(m):
                node = q.popleft()
                for u in graph[node]:
                    if u not in visited:
                        visited.add(u)
                        q.append(u)
        print(last, level)
        
        q = deque([last[0]])
        level = 0
        visited = set([last[0]])
        
        while q:
            m = len(q)
            level += 1
            for _ in range(m):
                node = q.popleft()
                for u in graph[node]:
                    if u not in visited:
                        visited.add(u)
                        q.append(u)
        return level -1

            
            
        
            
            
                    