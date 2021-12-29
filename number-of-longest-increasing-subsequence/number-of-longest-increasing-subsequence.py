class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        LIS, ct = [1] * n, [1] * n
        
        for i, num in enumerate(nums[1:], 1):
            for j in range(i):
                if nums[j] < num:
                    if LIS[j] + 1 > LIS[i]:
                        LIS[i] = LIS[j] + 1
                        ct[i] = ct[j]
                    elif LIS[j] + 1 == LIS[i]:
                        ct[i] += ct[j]
                        
        max_ = max(LIS)
        
        return sum(count for lis,count in zip(LIS, ct)  if lis == max_)