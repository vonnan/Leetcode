class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        
        UF = {i: i for i in range(n)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        res = n
        for t, a, b in logs:
            if find(a) == find(b):
                continue
            else:
                UF[find(a)] = find(b)
                res -= 1
                if res == 1:
                    return t
        return -1
                