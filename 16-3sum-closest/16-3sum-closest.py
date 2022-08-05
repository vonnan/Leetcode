class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res, n = inf, len(nums)
        nums.sort()
        
        n = len(nums)
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i-1]:
                continue
                
            j, k = i + 1, n - 1
            while j < k:
                sum3 = nums[j] + nums[k] + num
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                
                if sum3 == target:
                    return target
                
                elif sum3 > target:
                    k -= 1
                    
                else:
                    j += 1
                    
        return res