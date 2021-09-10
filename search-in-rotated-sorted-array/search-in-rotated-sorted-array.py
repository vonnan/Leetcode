class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[left]:
                if nums[left] <= target <=nums[mid]:
                    right = mid
                else:
                    left = mid + 1
                    
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            
        if nums[left] == target:
            return left
        else:
            return -1
        