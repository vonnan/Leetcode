from heapq import heappop
from heapq import heappush
from bisect import insort

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        dic = defaultdict(list)
        
        heap = []
        meetings.sort()
        available = list(range(n))
        
        for i in range(len(meetings)):
            
            s, e = meetings[i]
            
            while heap and heap[0][0] <= s:
                end, room = heappop(heap)
                insort(available, room)
        
            if available:
                room = available.pop(0)
                dic[room].append(e)
                heappush(heap, (e, room))
                
            else:
                end, room = heappop(heap)
                end += e - s
                heappush(heap, (end, room))
                dic[room].append(end)
        
        max_ = max(dic.values(), key = len)
        print(max_)
        
        for room in range(n):
            if dic[room] == max_:
                return room
                
                
                
            
        
        
        
        
        
        
        
        