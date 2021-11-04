from heapq import heappush
from heapq import heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, res = [], []
        for x,y in points:
            heappush(heap, (x*x + y * y, x,y))
            
        while k:
            _,x,y = heappop(heap)
            res.append((x,y))
            k -= 1
        
        return res