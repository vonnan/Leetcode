from heapq import heappush
from heapq import heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, n = [], len(nums)
        for i, num in enumerate(nums[:k]):
            heappush(heap, (-num, i))
        res = [-heap[0][0]]
        if heap[0][1] == 0:
            heappop(heap)
            
        for i in range(1, n- k + 1):
            heappush(heap, (-nums[i + k -1], i + k - 1))
            while heap[0][1] < i:
                heappop(heap)
            res.append(-heap[0][0])
        
        return res