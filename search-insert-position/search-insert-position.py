class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target <= nums[l]:
            return 0
        
        if target > nums[-1]:
            return r + 1
        
        while l < r:
            mid = (l + r)//2
            
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        return l
        
        
