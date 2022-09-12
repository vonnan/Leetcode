class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        
        nums = [num * (-1) ** (i % 2) for i, num in enumerate(nums)]
        n = len(nums)
        
        res = -inf
        print(nums)
        suffix = suf_max= suf_min = 0 
        
        for i in range(n-1, -1, -1):
            suffix += nums[i]
            
            sign = (-1) ** (i % 2)
            if sign == -1:
                res = max(res, suf_max - suffix)
            else:
                res = max(res, suffix - suf_min)
            
            suf_max = max(suf_max, suffix)
            suf_min = min(suf_min, suffix)
            
            
            
        return res
            
            
        
        