from heapq import heappush
from heapq import heappop
from heapq import heapify

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        heapify(sticks)
        
        res = 0
        while len(sticks) > 1:
            cost = heappop(sticks) + heappop(sticks)
            res += cost
            heappush(sticks, cost)
        
        return res 
            
        
        
        
