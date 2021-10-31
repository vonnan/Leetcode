class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        nums[:] = [0]* counter[0] + [1] * counter[1] + [2] * counter[2]
        