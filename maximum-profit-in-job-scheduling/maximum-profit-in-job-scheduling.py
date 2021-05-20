from bisect import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp_end = [0]
        dp_profit = [0]
        
        profit_time = sorted([(e,s,p) for e,s,p in zip(endTime, startTime, profit)])
        
        for e,s,p in profit_time:
            idx = bisect(dp_end, s)
            if dp_profit[-1]< dp_profit[idx-1] + p:
                dp_profit.append(dp_profit[idx-1] + p)
                dp_end.append(e)
                
        return dp_profit[-1]