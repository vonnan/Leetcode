class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        if nums[0] == target:
            return True
        if nums[-1] ==target:
            return right
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            
            if target > nums[right]:
                if nums[mid] > nums[right]:
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid
                else:
                    right -= 1
                    
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    if target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    right -= 1
        return True if nums[left] == target else False
