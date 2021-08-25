class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        left, right = 0, len(nums) - 1
        
        res = [-1, -1]
        
        if not nums:
            return res
        
        if target <nums[left] or target > nums[right]:
            return res
        
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        
        if target == nums[left]:
            res[0] = left
        else:
            return res
        
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right + 1)//2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid -1
                
        res[1] = right
        return res
            
                
            
        
                
                