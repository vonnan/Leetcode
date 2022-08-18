from heapq import heappush
from heapq import heappop

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        
        n = len(points)
        for i, pi in enumerate(points):
            xi, yi = pi
            for j, pj in enumerate(points[i+1:], i + 1):
                xj, yj = pj
                heappush(heap, (abs(xi- xj) + abs(yi - yj), i, j))
                
        res = 0
        n = len(points)
        if n == 1:
            return 0
        
        UF = {i:i for i in range(n)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        while heap:
            d, i, j = heappop(heap)
            if find(i) == find(j):
                continue
            union(i, j)
            res += d
            n -= 1
            if n == 1:
                return res