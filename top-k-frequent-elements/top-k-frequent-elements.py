from heapq import heappop
from heapq import heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key, val in counter.items():
            heappush(heap, (-val, key))
        
        res = []
        while k:
            _, num = heappop(heap)
            k -= 1
            res.append(num)
        return res
            