class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, sets = len(nums), set([])
        for i, num in enumerate(nums[:-2]):
            if i > 0 and num == nums[i-1]:
                continue
            target = - num
            j, k = i + 1, n-1
            
            if nums[i + 1] *2 > target or nums[-1] * 2 < target:
                continue
            
            while j < k:
                twosum = nums[j] + nums[k]
                if  twosum == target:
                    sets.add((num, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif twosum > target:
                    k -= 1
                else:
                    j += 1
        
        return sets
                