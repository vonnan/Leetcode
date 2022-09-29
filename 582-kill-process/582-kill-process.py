class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child = defaultdict(list)
        
        for a, b in zip(pid, ppid):
            child[b].append(a)
            
        q = deque([kill])
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            for c in child[node]:
                q.append(c)
        
        return res