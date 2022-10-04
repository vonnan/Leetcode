class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], A: List[int]) -> int:
        graph = defaultdict(set)
        A = set(A)
        for u, v in edges:
            if u not in A and v not in A:
                graph[u].add(v)
                graph[v].add(u)
        
        visited = set([0])
        q = deque([0])
        
        while q:
            
            node = q.popleft()
                
            for v in graph[node]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)
        
        return len(visited)
                