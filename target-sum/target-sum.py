class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = Counter({0:1})
        for num in nums:
            step = Counter()
            for key in counter:
                step[key + num] += counter[key]
                step[key - num] += counter[key]
            counter = step
                
                
        return counter[target]