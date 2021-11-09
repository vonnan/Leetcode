class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        lst = list(sorted(counter.keys()))
        dp = [0] * (len(counter) + 1)
        dp[1] = lst[0] * counter[lst[0]]
        for i, num in enumerate(lst[1:], 1):
            if num - lst[i - 1] == 1:
                dp[i + 1] = max(dp[i], dp[i- 1] + num * counter[num])
            else:
                dp[i + 1] = dp[i] + num * counter[num]
        return dp[-1]
            
            
        