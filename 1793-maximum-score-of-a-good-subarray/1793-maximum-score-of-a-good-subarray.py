from bisect import insort
from bisect import bisect_left
from heapq import heappush
from heapq import heappop

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        lst = [-1, n]
        
        for i, num in enumerate(nums):
            heappush(heap, (num, i))
            
        res = 0
        while heap:
            min_, i = heappop(heap)
            #print(min_, i, lst)
            idx = bisect_left(lst, i)
            if lst[idx-1] < k < lst[idx]:
                res = max(res, min_ * (lst[idx]- lst[idx-1] - 1))
            lst.insert(idx, i)
            
        return res
        
            
            
        
        
                
        