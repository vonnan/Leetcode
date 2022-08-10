class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, res = 0, inf
        tot = 0
        for i, num in enumerate(nums):
            tot += num
            if tot < target:
                continue
            while tot - nums[j] >= target:
                tot -= nums[j]
                j += 1
            
            res = min(res, i -j + 1)
            
        return res if res!= inf else 0