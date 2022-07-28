from heapq import heappush
from heapq import heappop

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = [0]
        
        for row in mat:
            new = []
            m = min(len(heap), k)
            for _ in range(m):
                num = heappop(heap)
                for x in row:
                    heappush(new, num + x)
            heap = new
        
        while k:
            num = heappop(heap)
            k -= 1
        return num
            