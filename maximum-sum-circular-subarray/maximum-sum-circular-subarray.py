from heapq import heappush
from heapq import heappop

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        presum, n, tot = [0], len(nums), sum(nums)
        suffsum = []
        min_, max_, res = 0, -inf, -inf
        dp_left, dp_right =[0] * n, [0] * n
        for i, num in enumerate(nums):
            nxt = presum[-1] + num
            res = max(res, nxt - min_)
            dp_left[i] = max_
            suffsum.append(tot - presum[-1])
            presum.append(presum[-1] + num)
            min_ = min(min_, presum[-1])
            max_ = max(max_, presum[-1])
        max_ = -inf    
        for i in range(n-1, -1, -1):
            dp_right[i] = max_
            max_ = max(max_, suffsum[i])
        
        for i in range(n):
            res = max(res, dp_left[i] + dp_right[i])
            
        return res if res !=-inf else -1
            
            
            
        
            
        