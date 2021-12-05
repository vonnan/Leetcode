class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        LIS, count = [1]* n, [1] * n
        
        for i, num in enumerate(nums[1:], 1):
            for j in range(i):
                if nums[j] < num:
                    if LIS[j] + 1 > LIS[i]:
                        LIS[i], count[i] = LIS[j] + 1, count[j]
                    elif LIS[j] + 1 == LIS[i]:
                        count[i] += count[j]
        
        max_ = max(LIS)
        
        return sum(ct for lis, ct in zip(LIS, count) if lis == max_)