from heapq import heappush
from heapq import heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
       
        
        for i, num in enumerate(nums[:k]):
            heappush(heap, (-num, i))
            
        res = [-heap[0][0]]
        
        for i, num in enumerate(nums[k:], k):
            heappush(heap, (-num, i))
            while heap and heap[0][1] <= i - k:
                heappop(heap)
            res.append(-heap[0][0])
        
        return res