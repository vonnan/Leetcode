class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = sorted(nums)
        n = len(nums)
        nums[::2] = lst[:(n+1)//2]
        nums[1::2] = lst[(n+1)//2:]
            