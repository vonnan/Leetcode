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
            nv, key = heappop(heap)
            res += -nv * key
        return res