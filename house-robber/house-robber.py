class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, nums[0]
        for num in nums[1:]:
            prev, curr = curr, max(curr, prev + num)
        return curr