class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        for i in range(n -1):
            for j in range(i+1, n):
                dp[(j, nums[j] - nums[i])] = max(dp[(i, nums[j] - nums[i])] + 1, dp[(j, nums[j] - nums[i])])
        #print(dp)
        return max(dp.values()) + 1
            