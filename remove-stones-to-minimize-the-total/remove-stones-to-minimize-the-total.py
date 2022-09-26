from heapq import heappush
from heapq import heappop

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        tot = sum(piles)
        
        heap = []
        for num in piles:
            heappush(heap, -num)
        
        while k:
            num = - heappop(heap)
            half = num//2
            tot -= half
            heappush(heap, half - num)
            k -= 1
        
        return tot