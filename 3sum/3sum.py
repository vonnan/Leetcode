class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), set([])
        for i in range(n-2):
            target = - nums[i]
            if target > 2* nums[-1] or target < 2* nums[i+1]:
                continue
            j, k = i + 1, n-1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
            
        return res
        
        
