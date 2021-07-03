class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[0] == target:
            return 0
        if nums[-1] ==target:
            return right
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if target > nums[right]:
                if nums[mid] > nums[right]:
                    if nums[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    if target > nums[mid]:
                        left = mid + 1
                    else:
                        right = mid
        return left if nums[left] == target else -1
                    
                