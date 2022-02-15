
class Solution:
    def maximumANDSum(self, nums: List[int], A: int) -> int:
        lst = list(range(1, A+1)) + list(range(1, A+1))
        n = len(nums) 
        nums.sort(reverse = 1)
        
        @cache
        def dp(i, mask):
            res = 0
            if i == n:
                return 0
            #print(i, bin(mask)[2:])
            
            for j, slot in enumerate(lst):
                if mask & (1 << j):
                    res = max(res, (nums[i] & slot) + dp(i+1, mask ^ (1<<j)))
            
            return res
        
        return dp(0, (1<< (2 * A)) - 1)
    
    
                              
            
            
                
                    
            
        
                           
                
                
                
                
                         
                         
                
        
        
        
        