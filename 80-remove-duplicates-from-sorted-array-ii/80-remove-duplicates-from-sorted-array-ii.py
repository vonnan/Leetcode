class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 2,2
        if len(nums) < 3:
            return len(nums)
        
        while fast < len(nums):
            if nums[slow-2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
            
        return slow
                
   
                
                
                