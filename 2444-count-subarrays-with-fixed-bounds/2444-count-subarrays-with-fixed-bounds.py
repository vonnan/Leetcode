class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        res = 0
        idx_bad, idx_min, idx_max = -1, -1, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                idx_bad = i
            
            if num == minK:
                idx_min = i
            
            if num == maxK:
                idx_max = i
                
            res += max(0, min(idx_min, idx_max) - idx_bad)
            
        return res
          
            
            
        
        
        
        
                