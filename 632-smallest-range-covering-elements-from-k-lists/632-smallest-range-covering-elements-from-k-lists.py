from heapq import heappush
from heapq import heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        row= len(nums)
        
        heap = []
        left = right = nums[0][0]
        
        for r in range(row):
            heappush(heap, (nums[r][0], r , 0))
            right = max(right, nums[r][0])
            left = min(left, nums[r][0])
          
        res = left, right
        d = right - left
        
        while heap:
            num, r, c = heappop(heap)
            
            c += 1
            if c == len(nums[r]):
                return res
            
            nxt = nums[r][c]
            heappush(heap, (nxt, r , c ))
            
            left, right = heap[0][0], max(right, nxt)
            if right - left < d:
                res = left, right
                d = right - left
            

            
         
        
        