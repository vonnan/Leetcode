from heapq import heappush
from heapq import heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap = []
        max_time = 0
    
            
        for t, end in courses:
            heappush(heap, -t)
            max_time += t
            if max_time > end:
                max_time += heappop(heap)
        return len(heap)
            