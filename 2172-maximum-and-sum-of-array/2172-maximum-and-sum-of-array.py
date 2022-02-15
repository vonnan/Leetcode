
class Solution:
    def maximumANDSum(self, nums: List[int], ns: int) -> int:
        n = len(nums) 
        
        @cache
        def dp(i, mask):
            res = 0
            if i == n:
                return 0
            
            for j in range(ns):
                b = 3 ** j
                if mask // b % 3 < 2:
                    res = max(res, (nums[i] & (j + 1)) + dp(i+1, mask + b))
            
            return res
        
        return dp(0, 0)
    
    
                              
            
            
                
                    
            
        
                           
                
                
                
                
                         
                         
                
        
        
        
        