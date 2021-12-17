from heapq import heappush
from heapq import heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        s,e = intervals[0]
        heap = [e]
        res = 1
        for s,e in intervals[1:]:
            if s < heap[0]:
                res += 1
                heappush(heap, e)
            else:
                heappop(heap)
                heappush(heap, e)
        return res
                