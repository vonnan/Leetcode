class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 1
        
        for i in range(len(nums)):
            ct = 0
            while nums[i] != -1:
                nums[i], ct, i = -1, ct + 1, nums[i]
            
            res = max(res, ct)
        
        return res
        
        
        