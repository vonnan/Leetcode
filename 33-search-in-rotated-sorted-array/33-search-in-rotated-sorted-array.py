from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        if nums == sorted(nums):
            idx = bisect_left(nums, target)
            if idx < len(nums) and nums[idx] == target:
                return idx
            return -1
        
        left, right = 0, len(nums) -1 
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[mid+1]:
                pivot = mid
                break
            else:
                left = mid + 1
        
        
        if target > nums[pivot] or target < nums[pivot + 1]:
            return -1
        
        elif target >= nums[0]:
            idx = bisect_left(nums[:pivot+ 1], target)
            if nums[idx] == target:
                return idx
            else:
                return -1
            
        else:
            idx = pivot + 1 + bisect_left(nums[pivot + 1:], target)
            if idx < len(nums) and nums[idx] == target:
                return idx
            else:
                return -1
                