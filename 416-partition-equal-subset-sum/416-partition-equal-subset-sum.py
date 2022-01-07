class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)//2
        nums.sort()
        sets = set([0])
        
        for num in nums:
            if num > target:
                return False
            
            if target - num in sets:
                return True
            
            sets |= set([num + x for x in sets if num + x < target])