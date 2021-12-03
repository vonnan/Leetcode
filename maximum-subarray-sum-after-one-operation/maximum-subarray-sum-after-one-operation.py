class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]* 2 for _ in range(n)]
        dp[0] = [ nums[0], nums[0] ** 2]
        res = dp[0][1]
        
        for i, num in enumerate(nums[1:] ,1):
            dp[i][0] = max(dp[i-1][0] + num, num)
            dp[i][1] = max(dp[i-1][0] + num * num, dp[i-1][1] + num, num * num)
        
            res = max(res, dp[i][1])
            
        return res