from heapq import heappush
from heapq import heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        while k:
            x = -heappop(heap)
            k -= 1
        return x