class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        
        dic = defaultdict(list)
        
        for u, v in connections:
            dic[u].append((v, False))
            dic[v].append((u, True))
            
        q = deque([0])
        visited = set([0])
        
        while q:
            node = q.popleft()
            for nei, boo in dic[node]:
                if nei not in visited:
                    if not boo:
                        res += 1
                    visited.add(nei)
                    q.append(nei)
        return res