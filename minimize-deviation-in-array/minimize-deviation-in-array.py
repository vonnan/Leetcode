from heapq import heappush
from heapq import heappop

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            if num %2 ==1:
                heappush(heap, -num * 2)
            else:
                heappush(heap, - num)
        
        small = - max(heap)
        res = inf
        # Now the top will be the maximum
        
        while len(heap) == len(nums):
            big = -heappop(heap)
            res = min(res, big - small)
            
            if big %2 ==0:
                heappush(heap, - big//2)
                small = min(small, big//2)
        return res