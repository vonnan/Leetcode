class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] =[num for num in nums if num != 0] + [ num for num in nums if num ==0]