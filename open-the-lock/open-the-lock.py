class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends or (target in deadends):
            return -1
        
        nxt = {str(i):[ str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        
        q = deque([target])
        
        seen = set([target])
        turn = 0
        while q:
            m = len(q)
            for _ in range(m):
                val = q.popleft()
                if val == "0000":
                    return turn
                for i in range(4):
                    for u in nxt[val[i]]:
                        nv = val[:i] + u + val[i+1:]
                        if (nv not in seen) and (nv not in deadends):
                            seen.add(nv)
                            q.append(nv)
                            if nv == "0000":
                                return turn + 1
            turn += 1
        return  -1
            
                    
            