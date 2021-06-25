from heapq import heappush
from heapq import heappop
from itertools import combinations
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap =[]
        for a,b in combinations(arr,2):
            heappush(heap, (a/b, a,b))
        
        for _ in range(k):
            ans = heappop(heap)
        
        return [ans[1], ans[2]]
        