class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        dp= [1]
        for num in nums:
            p *= num
            dp.append(p)
        
        dp = dp[:-1]
        
        dp2 = [1]
        p = 1
        n = len(nums)
        for i in range(n-1, -1, -1):
            
            p *= nums[i]
            dp2.append(p)
        
        dp2= dp2[::-1][1:]
        p
        return [a*b for a,b in zip(dp, dp2)]
            
        
            