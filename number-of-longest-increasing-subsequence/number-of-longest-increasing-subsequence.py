class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        LIS =[1] * n
        count = [1] *n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if LIS[i] == LIS[j] + 1:
                        count[i] += count[j]
                    elif LIS[i] < LIS[j] + 1:
                        LIS[i] = LIS[j] + 1
                        count[i] = count[j]
        max_ = max(LIS)
        print(max_, LIS, count)
        return sum(ct for lis, ct in zip(LIS, count) if lis == max_  )