from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        sep = sorted([(s,e,p) for s,e,p in zip(startTime, endTime, profit)])
        start =[ s for s, _, _ in sep]
        dp = [p for _,_, p in sep]
        n = len(start)
        
        for i in range(n-2, -1, -1):
            s,e,p = sep[i]
            idx = bisect_left(start, e)
            if idx != n:
                dp[i] = max(dp[i] + dp[idx], dp[i+1])
            else:
                dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]
                