class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        UF = {i:i for i in range(n)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        logs.sort()
        res = n
        for t,u,v in logs:
            if find(u) == find(v):
                continue
            else:
                res -= 1
                UF[find(u)] = find(v)
                if res == 1:
                    return t
        
        return -1