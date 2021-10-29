from heapq import heappush
from heapq import heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        lst = sorted([(w/q, q) for w, q in zip(wage, quality)])
        heap, qsum, res = [], 0, inf
        print(lst)
        for r, q in lst:
            heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heappop(heap)
            if len(heap) == K:
                res = min(res, r *qsum)
            print(r, qsum)
        return res
            
