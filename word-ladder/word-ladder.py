class Solution:
    def ladderLength(self, start: str, end: str, List: List[str]) -> int:
        if end not in List:
            return 0
        
        List = list(set([start] + List))
        
        nei = defaultdict(set)
        seen = set([end])
        n = len(start)
        
        for i, a in enumerate(List):
            for k in range(n):
                nei[a[:k] + "*" + a[k+1:]].add(a)
                
        q = deque([end])
        res = 1
        while q:
            res += 1
            m = len(q)
            for _ in range(m):
                word = q.popleft()
                for k in range(n):
                    new = word[:k] + "*" + word[k+1:]
                    for nxt in nei[new]:
                        if nxt == start:
                            return res
                        
                        if nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
        return 0
                            
        
        