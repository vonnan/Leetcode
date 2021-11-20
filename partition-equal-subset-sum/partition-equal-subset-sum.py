class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums)//2
        nums.sort()
        
        if nums[-1] > target:
            return False
        target -= nums[-1]
        if target == 0:
            return True
        nums = nums[:-1]
        
        sets = set([0])
        for num in nums:
            if num == target:
                return True
            if num > target:
                return False
            for x in list(sets):
                if num + x not in sets:
                    if num + x == target:
                        return True
                    else: 
                        sets.add(num + x)
        
        return False
                
        