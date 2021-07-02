from heapq import heappush
from heapq import heappop

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        heap = []
        
        for i, num in enumerate(nums):
            while heap and heap[0][1] < i - k:
                heappop(heap)
            dp[i] = num 
            
            if heap:
                dp[i] += -heap[0][0]
               
            if dp[i] >0:
                heappush(heap, (-dp[i], i))
             
        return max(dp)