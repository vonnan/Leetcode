class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return [key for key, val in Counter(nums).items() if val > 1][0]