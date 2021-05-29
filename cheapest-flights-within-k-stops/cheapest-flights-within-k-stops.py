from heapq import heappush
from heapq import heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = defaultdict(dict)
        for u,v,fare in flights:
            price[u][v] = fare
            
        seen = defaultdict(int)
        heap =[(0,src,k + 1)]
        
        while heap:
            cost, u, stop_budget = heappop(heap)
            
            if u == dst:
                return cost
            
            seen[u] = stop_budget
            
            if stop_budget >0:
            
                for nei in price[u]:
                    if nei in seen and seen[nei] >= stop_budget -1:
                        continue
                    
                    fare = price[u][nei]
                    heappush(heap, (cost + fare, nei, stop_budget -1))
                    
        return -1
                
                
            
            
            
            
            
            
        
        