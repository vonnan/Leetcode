class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in nums]
        dp[0] = [nums[0], nums[0]*nums[0]]
        
        res = nums[0]* nums[0]

        for i, num in enumerate(nums[1:], 1):
            dp[i][0] = max(dp[i-1][0] + num, num)
            dp[i][1] = max(num*num, dp[i-1][1] + num, dp[i-1][0] + num*num)
            res = max(res, dp[i][1])
    
        return res
            