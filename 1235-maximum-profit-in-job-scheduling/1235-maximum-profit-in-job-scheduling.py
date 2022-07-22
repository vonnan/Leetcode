from bisect import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sep = sorted([(s,e,p) for s,e,p in zip(startTime, endTime, profit)], key = lambda x: x[1])
        end = [e for  _,e, _ in sep]
        dp = [p for _,_,p in sep]
        n = len(sep)
        for i in range(1, n):
            s,e,p = sep[i]
            idx = bisect(end, s)
            if idx ==0:
                dp[i] = max(dp[i-1], p)
            else:
                dp[i] = max(dp[i-1], dp[idx -1] + p)
        
        return dp[-1]
                
                
            