class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2:
            return False
        
        target = tot//2
        nums.sort()
        
        if nums[-1] > target:
            return False
        
        sets = set([0])
        
        target -= nums[-1]
        if target ==0:
            return True
        
        for num in nums[:-1]:
            for prev in list(sets):
                if num + prev == target:
                    return True
                elif num + prev < target:
                    sets.add(num + prev)
        return False