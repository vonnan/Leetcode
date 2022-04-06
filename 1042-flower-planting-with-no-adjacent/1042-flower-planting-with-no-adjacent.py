class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        
        G = [[] for _ in range(n)]
        
        for u, v in paths:
            G[u - 1].append(v - 1)
            G[v - 1].append(u - 1)
            
        for u in range(n):
            res[u] = (set(range(1, 5)) - {res[v] for v in G[u] }).pop()
        
        return res
                