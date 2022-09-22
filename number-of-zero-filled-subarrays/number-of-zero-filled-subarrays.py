class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, ct = 0, 0
        
        for num in nums:
            if num:
                if ct:
                    res += ct * ( ct + 1)//2
                    
                ct = 0
            else:
                ct += 1
            
        
        if ct:
            res += ct * (ct + 1)//2
            
        return res
            
        