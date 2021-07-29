from heapq import heappush
from heapq import heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        res, speed_sofar, mod = 0, 0, 10**9 + 7
        
        for e,v in sorted(zip(efficiency, speed), reverse = 1):
            heappush(heap, v)
            speed_sofar += v
            if len(heap) > k:
                speed_sofar -= heappop(heap)
            res = max(res, e* speed_sofar)
        return res % mod