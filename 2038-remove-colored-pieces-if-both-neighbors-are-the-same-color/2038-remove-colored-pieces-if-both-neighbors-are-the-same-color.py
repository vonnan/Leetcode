from heapq import heappush
from heapq import heappop

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ct_a, ct_b = 0, 0
        
        heap_a, heap_b = [], []
        
        for c in colors:
            if c == "A":
                ct_a += 1
                if ct_b >= 3:
                    heappush(heap_b, -ct_b)
                ct_b = 0
            else:
                ct_b += 1
                if ct_a >= 3:
                    heappush(heap_a, -ct_a)
                ct_a = 0
        if ct_a >= 3:
            heappush(heap_a, -ct_a)
        if ct_b >=3:
            heappush(heap_b, -ct_b)
            
        flag = 1
        while True:
            if flag:
                if not heap_a:
                    return False
                
                nxt = heappop(heap_a) + 1
                if nxt <= -3:
                    heappush(heap_a, nxt)
            else:
                if not heap_b:
                    return True
                
                nxt = heappop(heap_b) + 1
                if nxt <= -3:
                    heappush(heap_b, nxt)
            
            flag = 1- flag
            
        
                
                
        
                
        
        
            
                
                
                            
            