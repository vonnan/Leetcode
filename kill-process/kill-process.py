class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent = defaultdict(int)
        child = defaultdict(list)
        
        for c,p in zip(pid, ppid):
            parent[c] = p
            child[p].append(c)
            
        res = []
        
        q = deque([kill])
        
        while q:
            node = q.popleft()
            res.append(node)
            for v in child[node]:
                q.append(v)
        return res