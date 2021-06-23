class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)
        
        if n < 3:
            return []
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
                
            j, k = i + 1, n-1
            target = - nums[i]
            
            while j < k:
                sum2 = nums[j] + nums[k]
                if sum2 > target:
                    k -= 1
                elif sum2 < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -=1
        
        return res