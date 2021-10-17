from heapq import heappush
from heapq import heappop

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        counter = Counter([1])
        nodes = set([1])
        clock = 0
        
        while counter[n] <2:
            
            if clock % (2 * change) >= change:
                clock += (change - clock % change)
            
            clock += time
            nodes = set([v for u in nodes for v in  graph[u] if counter[v] < 2])
            for v in nodes:
                counter[v] += 1
       
        return clock
            
               
                