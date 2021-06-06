from heapq import heappush
from heapq import heappop

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        speed_sum, res = 0, 0
        for e,s in sorted(zip(efficiency, speed), reverse = 1):
            heappush(heap, s)
            speed_sum += s
            if len(heap) >k:
                speed_sum -= heappop(heap)
            res = max(res, e*speed_sum)
        return res % (10**9 + 7)
            