from heapq import heappush
from heapq import heappop

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u,v,num in edges:
            graph[u][v] = num
            graph[v][u] = num
            
        heap = [(0, 0)]
        nodes = 0
        visited = set()
        
        while heap:
            cost, u = heappop(heap)
            if u in visited:
                continue
            
            visited.add(u)    
            nodes += 1
                
            for v, w in graph[u].items():
                nodes += min(maxMoves - cost, w)    
                if v not in visited:    
                    if w + cost  >= maxMoves:
                        graph[v][u] -= maxMoves - cost
                    else:
                        heappush(heap, (w + cost +1, v))
                        del graph[v][u]
            
        return nodes
                
                

                
                
                
                    
                
                    
