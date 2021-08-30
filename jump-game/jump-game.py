class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, start, max_reach = len(nums), 0, 0
        
        while start <= max_reach and start < n: 
            if max_reach >= n-1:
                return True
            
            max_reach = max(max_reach, start + nums[start])
            
            start += 1
            
        return False
            