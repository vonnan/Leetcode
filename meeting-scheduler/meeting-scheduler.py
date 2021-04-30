from heapq import heapify
from heapq import heappop

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapify(heap)
        
        if not heap: 
            return []
        
        s1, e1 = heappop(heap)
        
        while heap:
            while heap and heap[0][0] >= e1:
                s1, e1 = heappop(heap)
            if heap: 
                s, e = heappop(heap)
                left = max(s1, s)
                right = min(e1, e)
                if right - left >= duration:
                    return [left, left + duration]
                s1, e1 = s, e
        return []
            
        