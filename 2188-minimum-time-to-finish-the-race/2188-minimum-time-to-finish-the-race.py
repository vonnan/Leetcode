
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        dp = [inf] * (numLaps + 1)
        dp[0] = 0
        
        for f,r in tires:
            tot = f
            tire = 1
            cost = f
            while tire < min(17, numLaps + 1):
                dp[tire] = min(dp[tire], tot)
                cost *= r
                tot += cost
                tire += 1
       
        for i in range(1, numLaps + 1):
            for j in range(1, i):
                dp[i] = min(dp[i], changeTime + dp[j] + dp[i - j])
        
        return dp[-1]