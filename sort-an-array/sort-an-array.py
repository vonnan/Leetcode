class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            
            pivot = nums[len(nums)//2]
            
            left = [x for x in nums if x < pivot]
            mid = [x for x in nums if x == pivot]
            right =  [x for x in nums if x > pivot]
            
            return quickSort(left) + mid + quickSort(right)
        
        nums = quickSort(nums)
        
        return nums
        