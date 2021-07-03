class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        if len(nums)==1:
            return [0, 0] if nums[0] == target else [-1, -1]
        left, right = 0, len(nums) - 1
        res = [-1, -1]
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            res[0] = left
        else:
            return res
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right + 1)//2
            if nums[mid] <= target:
                left = mid
            else: 
                right = mid - 1
        
        if nums[right] == target:
            res[1] = right
            
        return res