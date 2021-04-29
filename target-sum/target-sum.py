from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = Counter({0 : 1})
        
        for num in nums:
            step = Counter()
            for key in count:
                step[key + num] += count[key]
                step[key - num] += count[key]
            count = step
        
        return count[target]
            
        
        