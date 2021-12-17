class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2:
            return False
        
        sets = set([0])
        target = sum(nums)//2
        nums.sort()
        
        for num in nums:
            if target - num in sets:
                return True
            sets |= set([num + x for x in sets if num + x < target])
        return False
        