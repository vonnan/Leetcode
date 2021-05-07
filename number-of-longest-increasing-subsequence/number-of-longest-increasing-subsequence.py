class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS, count = [1]*n, [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[i] == LIS[j] + 1:
                        count[i] += count[j]
                    elif LIS[i] < LIS[j] + 1:
                        LIS[i] = LIS[j] + 1
                        count[i] = count[j]
        print(LIS, count)                
        return sum(cnt for lis, cnt in  zip(LIS, count) if lis == max(LIS))
                        
                    
                    
                
        