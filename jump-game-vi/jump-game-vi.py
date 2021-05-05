from heapq import heappush
from heapq import heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        heap =[(0, -k)]
        
        for i, num in enumerate(nums):
            while heap and i - heap[0][1] > k:
                heappop(heap)
            num -= heap[0][0]
            heappush(heap, (-num, i))
            
        return num
        
        
        
        