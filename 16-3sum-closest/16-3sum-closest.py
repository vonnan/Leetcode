class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if sum(nums[:3]) >= target:
            return sum(nums[:3])
        
        if sum(nums[-3:]) <= target:
            return sum(nums[-3:])
        
        n = len(nums)
        res = sum(nums[:3])
        
        for i, num in enumerate(nums[:-2]):
            if num * 3 - target > abs(res - target):
                return res
            
            j, k = i + 1, n - 1
            
            while j < k:
                sum3 = num + nums[j] + nums[k]
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                    
                if sum3 == target:
                    return sum3
                
                if sum3 > target:
                    k-=1
                
                else:
                    j += 1
                    
        return res