from heapq import heappush
from heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        for _ in range(k-1):
            heappop(heap)
        return -heap[0]