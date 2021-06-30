class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                nums[i] = "_"
            else:
                prev = nums[i]
        print(nums)
        nums[:] = [num for num in nums if num != "_"]
        
        return len(nums)