from bisect import bisect

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        n = len(nums)
        
        if n ==1:
            return nums
        
        for i in range(n-1,0,-1):
            if nums[i-1] >= nums[i]:
                continue
            elif i==len(nums)-1:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                return nums
            else:
                idx = bisect(nums[i:][::-1], nums[i-1])+1
                
                nums[i-1], nums[-idx] = nums[-idx], nums[i-1]
               
                nums[i:] = [n for n in reversed(nums[i:])]
                
                return nums
        nums.reverse()
        return nums
      