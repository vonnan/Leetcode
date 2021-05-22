class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return min(nums)
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid +1 
            else:
                right = mid
            if right - left <=2:
                return min(nums[left:right+1])
        return nums[left]
                
        