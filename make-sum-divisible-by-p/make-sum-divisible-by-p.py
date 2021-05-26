from collections import defaultdict
from itertools import accumulate

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dp = defaultdict(list)
        remainder = sum(nums)%p
        dp[0], prev, res = -1, 0, len(nums)
        for i, num in enumerate(nums):
            curr = (prev + num)%p
            dp[curr] = i
            need = (curr - remainder)%p
            if need in dp:
                res = min(res, i- dp[need])
            prev = curr
        return res if res < len(nums) else -1 
            
            
            
        
        
              
                
        