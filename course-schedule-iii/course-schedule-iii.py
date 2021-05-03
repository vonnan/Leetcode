from heapq import heappush
from heapq import heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        
        max_time = 0
        heap = []
        
        for duration, end in courses:
            max_time += duration
            heappush(heap, -duration)
            if max_time > end:
                max_time += heappop(heap)
                
        return len(heap)
        
        
        
        