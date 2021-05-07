from collections import defaultdict
from heapq import heappop
from heapq import heappush
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        w = collections.defaultdict(dict)
        for u, v, p in flights:
            w[u][v] = p
        heap = [(0, src, K + 1)]
        seen = defaultdict(int)
        while heap:
            p, u, K = heapq.heappop(heap)
            seen[u] = K
            if u == dst:
                return p
            if K > 0:
                for v in w[u]:
                    if v in seen and seen[v] >= K-1:
                        continue
                    heapq.heappush(heap, (p + w[u][v], v, K - 1))
        return -1