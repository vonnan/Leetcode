from heapq import heappush
from heapq import heappop
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [inf] * n
        for i, r in enumerate(ranges):
            for j in range(max(i-r+1,0), min(i+r, n) + 1):
                dp[j] = min(dp[j], dp[max(i-r,0)] + 1)
        return dp[n] if dp[n] != inf else -1
            
            
                
                
            
            
        