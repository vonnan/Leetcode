from heapq import heappush
from heapq import heappop
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        heap = []
        
        events.sort()
        
        for _,e,val in events:
            heappush(heap, (e, val))
        
        pre_max, res = 0, 0
        
        for s,e,v in events:
            while heap:
                end, val = heappop(heap)
                if end >= s:
                    heappush(heap, (end, val))
                    break
                pre_max = max(pre_max, val)
            res = max(res, v + pre_max)
            
        return res
                
            
        
        
          
            