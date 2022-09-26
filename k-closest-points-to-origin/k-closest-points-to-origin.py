from heapq import heappush
from heapq import heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for a, b in points:
            heappush(heap, (a **2 + b**2, a, b))
            
        res = []
        while k:
            _,a,b = heappop(heap)
            res.append((a, b))
            k -= 1
        
        return res