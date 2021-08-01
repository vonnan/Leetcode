from heapq import heappush
from heapq import heappop
from heapq import heapify
class Solution:
    def numberOfWeeks(self, A: List[int]) -> int:
        """
        if len(milestones) ==1:
            return 1
        heap, res = [], 0
        for m in milestones:
            heappush(heap, -m)
        
        while len(heap) > 1:
            first = heappop(heap)
            second = heappop(heap)
            res -= second * 2
            if first != second:
                heappush(heap, first - second)
        
        if len(heap) ==0:
            return res
        
        else:
            return res + 1
        """
        
        _sum, _max = sum(A), max(A)
        if _sum >= 2* _max:
            return _sum
        
        else:
            return 2*(_sum - _max) + 1
        
        