from heapq import heappush
from heapq import heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for i, p in enumerate(points):
            x, y = p
            heappush(heap, (x*x + y * y, i))
        res = []
        for _ in range(k):
            res.append(points[heappop(heap)[1]])
        return res