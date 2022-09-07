class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start, max_ = 0, 0
        while start <= max_ and start < n:
            max_ = max(max_, nums[start] + start)
            start += 1
            if max_ >= n -1:
                return True
        return False
                
        
        