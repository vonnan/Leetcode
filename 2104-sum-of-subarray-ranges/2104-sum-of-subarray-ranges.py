class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n - 1):
            min_, max_ = nums[i], nums[i]
            for j in range(i + 1, n):
                if nums[j] < min_:
                    min_ = nums[j]
                if nums[j] > max_:
                    max_ = nums[j]
                res += max_ - min_
        return res
                
                