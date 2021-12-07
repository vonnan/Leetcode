from heapq import heappop
from heapq import heappush

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = [(0, -1)]
        presum, res  = 0, inf
        
        for i, num in enumerate(nums):
            presum += num
            target = presum - k
            
            while heap and heap[0][0] <= target:
                psum, idx = heappop(heap)
                res = min(res, i - idx)
            
            heappush(heap, (presum, i))
        
        return res if res != inf else -1
        