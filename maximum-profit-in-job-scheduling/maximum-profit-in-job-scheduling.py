
from bisect import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp_end = [0]
        dp_profit = [0]
        # endtime, profit
        lst = sorted([(e,s,p) for  s,e,p in zip(startTime, endTime, profit)])
        for e,s,p in lst:
            idx = bisect(dp_end, s)
            if dp_profit[idx-1] + p > dp_profit[-1]:
                dp_end.append(e)
                dp_profit.append(dp_profit[idx-1] + p)
                
        return dp_profit[-1]
            
            
            
        