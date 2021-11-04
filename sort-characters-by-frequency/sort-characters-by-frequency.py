from heapq import heappush
from heapq import heappop

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        
        for key, val in counter.items():
            heappush(heap, (-val, key))
        
        res = ""    
        while heap:
            val, key = heappop(heap)
            res += (-val) * key
        
        return res