from bisect import bisect_left
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [Counter([]) for _ in range(n)]
        res = 0
        
        for i, num in enumerate(nums):
            for j in range(i):
                dp[i][num - nums[j]] += dp[j][num - nums[j]] + 1
            res += sum(dp[i].values())
            
        return res - n * (n - 1)//2
        
            
        