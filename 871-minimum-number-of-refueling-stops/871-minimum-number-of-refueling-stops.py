from heapq import heappush
from heapq import heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = [(-startFuel, -1)]
        if startFuel >= target:
            return 0
        visited = set()
        stations.sort()
        while heap:
            
            cost, sta_id = heappop(heap)
            visited.add(sta_id)
            if -cost >= target:
                return len(visited)-1
            flag = False
            for i, st in enumerate(stations):
                
                if st[0] <= -cost and (i not in visited):
                    heappush(heap, (-st[1] + cost, i))
                    flag = True
            if not flag:
                return -1
        return -1
                
            
                    
                
                    