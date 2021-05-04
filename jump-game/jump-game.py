class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, start, max_jump = len(nums), 0, 0
        
        
        while start <= max_jump and start < n-1:
            if max_jump >= n-1:
                return True
            max_jump = max(max_jump, start + nums[start])
            start += 1
            
            
        return max_jump >= n-1
            
                    
                
        