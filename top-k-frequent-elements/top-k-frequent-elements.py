from heapq import heappop
from heapq import heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap, res = [], []
        for key, val in counter.items():
            heappush(heap, (-val, key))
        for _ in range(k):
            res.append(heappop(heap)[1])
        return res