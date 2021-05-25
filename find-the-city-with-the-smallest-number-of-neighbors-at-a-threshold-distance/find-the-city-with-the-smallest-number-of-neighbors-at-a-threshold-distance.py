from heapq import heappush
from heapq import heappop
from collections import defaultdict
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        def helper(city):
            dist = {}
            heap = [(0, city)]
            
            while heap:
                curr_w, u = heappop(heap)
                if u in dist:
                    continue
                
                if u != city:
                    dist[u] = curr_w
                    
                for nei, w in graph[u]:
                    if nei in dist:
                        continue
                    if curr_w + w <= distanceThreshold:
                        heappush(heap, (curr_w + w, nei))
                        
            return len(dist)
        
        count = n
        
        for i in range(n):
            ct = helper(i)
            if count >= ct:
                res = i
                count = ct
        return res
            
       
        