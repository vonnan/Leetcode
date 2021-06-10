from bisect import insort
from bisect import bisect_left
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = [i for i in range(k)]
        heap_end_time = []
        busy_servers = [0]* k
        busiest = 0
        
        for i, a in enumerate(arrival):
            while heap_end_time and heap_end_time[0][0] <= a:
                _, curr_server = heappop(heap_end_time)
                insort(available, curr_server)
                 
            if not available:
                continue
            
            curr_idx = bisect_left(available, i% k) % (len(available))
            
            curr_server = available[curr_idx]
            
            busy_servers[curr_server] += 1
            busiest = max(busiest, busy_servers[curr_server])
            
            available.pop(curr_idx)
            
            heappush(heap_end_time, (a+load[i], curr_server))
            
        
        res = []    
        for i, b in enumerate(busy_servers):
            if b == busiest:
                res.append(i)
        return res
            
        
                
                
        