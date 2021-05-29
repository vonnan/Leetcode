from itertools import accumulate
from collections import Counter
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = list(accumulate([0] + nums))
        counter = Counter(presum)
        
        res = 0
        if goal ==0:
            return sum(val*(val-1)//2 for _, val in counter.items())
        
        for key in sorted(counter.keys()):
            if key - goal in counter:
                res += counter[key] * counter[key - goal]
                
        return res
