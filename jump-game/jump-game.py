class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start, max_reach, n = 0, 0, len(nums)
        if n==1:
            return True
        while start <= max_reach and start <n:
            max_reach = max(max_reach, nums[start] + start)
            if max_reach >= n-1:
                return True
            
            start += 1
            
        return False