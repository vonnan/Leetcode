class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        
        tot = sum(nums)
        target = tot//2
        
        if tot%2 or nums[-1] > target:
            return False
        
        if target in set(nums):
            return True
        
        sets = set([nums[0]])
        for num in nums[1:]:
            if num + nums[0] > target:
                return False
            for x in list(sets):
                if num + x not in sets:
                    sets.add(num + x)
                    if num + x == target:
                        return True
        return False
        
        
            