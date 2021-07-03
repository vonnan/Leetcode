class Solution:
    def hIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if nums[-1] < 1:
            return 0
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= len(nums)- mid:
                right = mid
            else:
                left = mid + 1
        return len(nums) - left
                