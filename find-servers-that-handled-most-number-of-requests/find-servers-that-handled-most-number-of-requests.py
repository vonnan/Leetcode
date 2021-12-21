from bisect import bisect_left
from bisect import insort
from heapq import heappush
from heapq import heappop

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        ready = list(range(k))
        busy =[0] * k
        busiest = 0
        heap = []
        
        for i, t in enumerate(arrival):
            while heap and heap[0][0] <= t:
                _, server = heappop(heap)
                insort(ready, server)
            
            if not ready:
                continue
                
            idx = bisect_left(ready, i%k) %(len(ready))
            
            server = ready[idx]
            
            busy[server] += 1
            
            busiest = max(busiest, busy[server])
            heappush(heap, (t + load[i], server))
            ready.pop(idx)
            
            
        res = []
        
        for i, b in enumerate(busy):
            if b == busiest:
                res.append(i)
        
        return res