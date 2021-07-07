from heapq import heappush
from heapq import heappop
from bisect import insort

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            heappush(heap, (abs(x-a),a))
        
        res = []
        for _ in range(k):
            if not res:
                res.append(heappop(heap)[1])
            else:
                insort(res, heappop(heap)[1])
        return res
                     