class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums += [0]
        dp = [0] * len(nums) 
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i, num in enumerate(nums[2:], 2):
            dp[i] = max(dp[i-2] + num, dp[i-1])
        print(dp)
        return dp[-1]