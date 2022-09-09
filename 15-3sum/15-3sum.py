class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set([])
        print(nums)
        n = len(nums)
        for i, num in enumerate(nums[:-2]):
            target = -num
            if i and num == nums[i-1]:
                continue
            
            if nums[i+ 1] * 2 > target or nums[-1] * 2 < target:
                continue
            j, k = i + 1, n - 1
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
        