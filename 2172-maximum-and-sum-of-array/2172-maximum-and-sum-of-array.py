
class Solution:
    #def maximumANDSum(self, nums: List[int], A: int) -> int:
    def maximumANDSum(self, A: List[int], ns: int) -> int:
        @cache
        def dp(i, mask):
            if i == len(A): return 0
            res = 0
            for slot in range(ns):
                t = 3 ** slot
                if ((mask // t) % 3):
                    res = max(res, dp(i + 1, mask - t) + (A[i] & (slot+1)))
            return res
        return dp(0, 3 ** ns -1)                    
            
        
                           
                
                
                
                
                         
                         
                
        
        
        
        