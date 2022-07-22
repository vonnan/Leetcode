class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        max_ = max(nums)
        counter = Counter(nums)
        dp = [0] * (max_ + 1)
        
        for num in counter:
            for x in range(num, max_ + 1, num):
                dp[x] += counter[num]
        
        linear = list(accumulate(dp))
        
        return sum(linear[num] for num in nums) % (10**9 + 7)
            