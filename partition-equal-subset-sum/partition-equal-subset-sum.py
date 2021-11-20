class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums)//2
        nums.sort()
        
        if nums[-1] > target:
            return False
        
        sets = set([0])
        
        for num in nums:
            for x in list(sets):
                if num + x == target:
                    return True
                
                elif num + x > target:
                    break
                else: 
                    sets.add(num + x)
        
        return False
                
        