from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = [-inf] + days
        n = len(days)
        dp = [inf] * n
        dp[0] = 0
        
        for i, day in enumerate(days[1:], 1):
            idx_7 = bisect_left(days, day - 6)-1
            idx_30 = bisect_left(days, day - 29)-1
            dp[i] = min(dp[i-1] + costs[0], dp[idx_7] + costs[1], dp[idx_30] + costs[2])
        
        return dp[-1]