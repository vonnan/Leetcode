
from heapq import heappush
from heapq import heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        lst = sorted([(c,p) for c,p in zip(capital, profits)], reverse = 1)
        res = 0
        heap = []
    
        while lst or heap:
            if not heap and lst[-1][0] > w:
                return res
            if heap:
                w += -heappop(heap)
                k-= 1
                res = w
                if k ==0:
                    return res
            while lst and lst[-1][0] <= w:
                c, p = lst.pop()
                heappush(heap, -p)
            
            
        return res        