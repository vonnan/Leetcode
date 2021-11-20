from bisect import bisect_left
class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        n = len(days)
        dp =[inf] * (n+1)
        dp[0], dp[1] = 0, min(cost)
        for i, day in enumerate(days[1:],2):
            idx_7 = bisect_left(days, day - 6)
            idx_30 = bisect_left(days, day - 29)
            dp[i] = min(dp[i-1] + cost[0], dp[idx_7] + cost[1], dp[idx_30] + cost[2])
            
        return dp[-1]
            
            
            