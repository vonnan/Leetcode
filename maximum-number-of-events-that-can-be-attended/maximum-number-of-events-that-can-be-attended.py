from heapq import heappush
from heapq import heappop

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = []
        
        events.sort(reverse = 1)
        res, day = 0, 0
        
        while events or heap:
            if not heap:
                day = events[-1][0]
                
            while events and events[-1][0] <= day:
                heappush(heap, events.pop()[1])
            
            heappop(heap)
            
            res += 1
            day += 1
            
            while heap and heap[0] < day:
                heappop(heap)
                
        return res
        
        
            
                
            