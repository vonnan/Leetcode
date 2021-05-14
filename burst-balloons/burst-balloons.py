class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        def maxcoin(nums, memo = {}):
            if nums not in memo:
                first , last = nums[0], nums[-1]
                ans = max([maxcoin(nums[:k+1]) + maxcoin(nums[k:]) + first * nums[k] * last for k in range(1, len(nums)-1)] or [0])
                memo[nums] = ans
            return memo[nums]
        
        return maxcoin(tuple([1] + nums + [1]))
                