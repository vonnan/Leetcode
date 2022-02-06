class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        
        slow, fast = 2, 2
        while fast < n:
            if nums[slow -2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
            
        return slow