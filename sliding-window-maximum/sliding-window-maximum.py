from heapq import heappush
from heapq import heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, n = [], len(nums)
        for i in range(k):
            heappush(heap, (-nums[i], i))
        
        res = [-heap[0][0]]
        
        for i in range(1, n-k+1):
            heappush(heap, (-nums[i + k -1], i + k -1))
            
            while heap and heap[0][1]<= i -1:
                heappop(heap)
            res.append(-heap[0][0])
        
        return res
            
            
        
            