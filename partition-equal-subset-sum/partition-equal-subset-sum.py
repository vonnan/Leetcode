class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        target = tot//2
        nums.sort()
        
        if tot%2 or target < nums[-1]:
            return False
        
        target -= nums[-1]
        
        if target ==0 or target in set(nums[:-1]):
            return True
        sets =set([0])
        for num in nums[:-1]:
            if num > target:
                return False
            for prev in list(sets):
                if prev + num not in sets:
                    if num + prev == target:
                        return True
                    
                    sets.add(prev + num)
            
        return False
            
