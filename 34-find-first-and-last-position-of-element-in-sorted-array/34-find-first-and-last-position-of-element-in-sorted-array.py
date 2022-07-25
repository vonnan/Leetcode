class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        left, right = 0, n -1
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] != target:
            return [-1, -1]
        
        res = [left, left]
        
        left, right = 0, n-1

        while left < right:
            mid = (left + right + 1)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid -1
        
        res[1] = left
        return res