class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start, max_reach, n = 0, 0, len(nums)
        while start <= max_reach and start < n:
            max_reach = max(max_reach, start + nums[start])
            start +=1
            if max_reach >= n-1:
                return True
        return False