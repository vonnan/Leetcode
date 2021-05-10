def isPossible(self, A):
        total = sum(A)
        A = [-a for a in A]
        heapq.heapify(A)
        while True:
            a = -heapq.heappop(A)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(A, -a)
            
from heapq import heappush
from heapq import heappop

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        tot = sum(target)
        heap = []
        for t in target:
            heappush(heap, -t)
        
        while True:
            next_tot = - heappop(heap)
            tot -= next_tot
            if tot == 1 or next_tot ==1:
                return True
            if next_tot < tot or tot ==0 or next_tot % tot ==0:
                return False
            next_tot %= tot
            tot += next_tot
            heappush(heap, -next_tot)