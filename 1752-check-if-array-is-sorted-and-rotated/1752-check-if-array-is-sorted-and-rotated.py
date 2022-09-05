class Solution:
    def check(self, nums: List[int]) -> bool:
        nxt = sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == nxt:
                return True
        return False
            