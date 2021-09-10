class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) -1
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] != target:
            return [-1, -1]
        
        res = [left, left]
        
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1)//2
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid
        res[1] = left
        return res
        
            