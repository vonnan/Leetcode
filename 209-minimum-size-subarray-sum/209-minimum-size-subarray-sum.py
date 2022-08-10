class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, n, tot = 0, len(nums), 0
        if sum(nums) < target:
            return 0
        
        res = inf
        for r, num in enumerate(nums):
            tot += num
            if tot >= target:
                while tot >= target:
                    tot -= nums[l]
                    l += 1
                res = min(res, r - l + 2)
        return res
                