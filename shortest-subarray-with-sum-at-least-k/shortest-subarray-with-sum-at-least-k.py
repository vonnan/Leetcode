from heapq import heappush
from heapq import heappop

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        presum = 0
        heap = [(0,-1)]
        res = len(A) + 1
        
        for i,a in enumerate(A):
            presum += a
            diff = presum -K
            
            while heap and heap[0][0] <= diff:
                psum,idx = heappop(heap)
                res = min(res, i - idx )
            
            heappush(heap, (presum, i))
            
        return res if res <= len(A) else -1