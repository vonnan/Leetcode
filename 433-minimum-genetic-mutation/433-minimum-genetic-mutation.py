class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        
        if end not in bank:
            return -1
        
        bank = list(set(bank)) + [start]
        
        graph = defaultdict(list)
        for i, b in enumerate(bank):
            for j, c in enumerate(bank[i+1:], i + 1):
                for k in range(8):
                    if b[:k] + b[k+1:] == c[:k] + c[k+1:]:
                        graph[b].append(c)
                        graph[c].append(b)
                        break
        
        if not graph[start]:
            return -1
        
        seen = set([])
        res = -1
        q = deque([start])
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                node = q.popleft()
                if node == end:
                    return res
                
                seen.add(node)
                for u in graph[node]:
                    if u not in seen:
                        q.append(u)
                        
        return -1
                        
        