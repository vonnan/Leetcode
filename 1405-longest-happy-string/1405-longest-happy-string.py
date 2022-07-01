from heapq import heappush
from heapq import heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heappush(heap, (-a, "a"))
        if b:
            heappush(heap, (-b, "b"))
        if c :
            heappush(heap, (-c, "c"))
        
        res = ""
        while heap:
            neg, char = heappop(heap)
            if not heap and (len(res) > 1 and res[-1] == char and res[-2] == char):
                return res
            if not res or len(res) == 1 or (res[-1] != char) or (len(res) > 1 and res[-2] != char) :
                res += char
                neg += 1
                if len(res) > 1 and res[-1] == char and res[-2] == char:
                    if not heap:
                        return res
                    else:
                        n, ch = heappop(heap)
                        res += ch
                        n += 1
                        if n:
                            heappush(heap, (n, ch))
            if neg:
                heappush(heap, (neg, char))
        return res
                
        
                        
                    
            
        
        