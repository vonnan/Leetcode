class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        tot = sum(nums)
        if tot %2 or nums[-1] > tot//2:
            return False
        
        target = tot//2 - nums.pop()
        if not target:
            return True
        
        sets = set([0])
        
        for num in nums:
            sets |= set([num + x for x in sets])
            if target in sets:
                return True
        return False
                
        
        
       