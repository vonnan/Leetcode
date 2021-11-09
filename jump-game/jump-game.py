class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start, max_reach = 0, 0
        while start <= max_reach and start < n:
            max_reach = max(max_reach, start + nums[start])
            start += 1
            if max_reach >= n-1:
                return True
        return False
        
            
        
        