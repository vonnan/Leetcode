
class Solution:
    #def maximumANDSum(self, nums: List[int], A: int) -> int:
    def maximumANDSum(self, A: List[int], ns: int) -> int:
        @cache
        def dp(i, mask):
            if i == len(A): return 0
            res = 0
            for slot in range(1, ns+1):
                b = 10 ** (slot -1)
                if ((mask // b) % 10) < 2:
                    res = max(res, dp(i + 1, mask + b) + (A[i] & slot))
            return res
        return dp(0, 0)                    
            
        
                           
                
                
                
                
                         
                         
                
        
        
        
        