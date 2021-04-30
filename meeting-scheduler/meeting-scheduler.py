from heapq import heappush
from heapq import heappop

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = []
        for s1, e1 in slots1:
            if e1 - s1 >= duration:
                heappush(heap, (s1, e1))
           
        for s2, e2 in slots2:
            if e2- s2 >= duration:
                heappush(heap, (s2, e2))   
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
                    return [ left, left + duration]
                s1, e1 = s, e
        return []
            
        