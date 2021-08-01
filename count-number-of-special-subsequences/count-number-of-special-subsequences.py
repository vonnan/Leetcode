class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [1,0,0,0]
        mod = 10**9 + 7
        
        for num in nums:
            dp[num +1] += dp[num] + dp[num + 1]
        
        return dp[-1] % mod
            
                
                