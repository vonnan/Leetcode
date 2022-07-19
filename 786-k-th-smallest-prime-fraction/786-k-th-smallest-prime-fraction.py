from heapq import heappush
from heapq import heappop

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        heap = []
        
        n = len(arr)
        for i, a in enumerate(arr):
            for j in range(i + 1, n):
                heappush(heap, (a/arr[j], i, j))
        
        while heap:
            val, i, j = heappop(heap)
            k -= 1
            if not k:
                return (arr[i], arr[j])