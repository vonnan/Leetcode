class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        
        for i, num in enumerate(nums[1:], 1):
            dp[i+1] = max(dp[i], dp[i-1] + num)
        
        return dp[-1]