from itertools import combinations
from heapq import heappush
from heapq import heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for x,y in combinations(arr,2):
            heappush(heap, (x/y,x,y))
        for _ in range(k-1):
            heappop(heap)
        _, x, y = heappop(heap)
        return [x,y]
        
            