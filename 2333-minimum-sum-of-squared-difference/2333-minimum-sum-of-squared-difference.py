from heapq import heappush
from heapq import heappop

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        lst = [abs(a-b) for a,b in zip(nums1, nums2)]
        if sum(lst) <= k:
            return 0
        counter = Counter(lst)
        heap = [(0, 0)]
        
        for key, val in counter.items():
            heappush(heap, (-key, val))
          
        while k:
            neg, val = heappop(heap)
            if k // val >= heap[0][0] - neg:
                first, v = heappop(heap)
                k -= (first - neg)* val
                heappush(heap, (first, val + v))
            else:
                q,r = divmod(k, val)
                nxt = neg + q
                heappush(heap, (nxt, val - r))
                heappush(heap, (nxt + 1, r))
                break
        
        return sum(neg**2 * val for neg, val in heap)
                
                