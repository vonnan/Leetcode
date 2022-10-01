from heapq import heappush
from heapq import heappop

class Solution:
    def getSkyline(self, A: List[List[int]]) -> List[List[int]]:
        lst = sorted([(l, -h, r) for l, r, h in A] + list(set((r, 0, 0) for _, r, _ in A)))
        res, heap =[(0,0)], [(0, inf)]
        print(lst)
        for l, nH, r in lst:
            while l >= heap[0][1]:
                heappop(heap)
            if nH:
                heappush(heap, (nH, r))
            
            if res[-1][1] + heap[0][0]:
                res.append((l, -heap[0][0]))
        
        return res[1:]
                   