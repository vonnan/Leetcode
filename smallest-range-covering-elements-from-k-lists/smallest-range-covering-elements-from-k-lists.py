from heapq import heappush
from heapq import heappop
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left, right = -10**6, 10**6
        heap = []
        for i, row in enumerate(nums):
            heappush(heap, (row[0], i, 0))
        res = left, right   
        right = max(row[0] for row in nums)
        print(heap, left, right)
        while heap:
            left, i, j = heappop(heap)
            if right - left < res[1] - res[0]:
                res = left, right
                if right - left == 0:
                    return left, right
                
            if j == len(nums[i]) -1:
                return res
            
            nxt = nums[i][j+1]
            
            right = max(right, nxt)
            
            heappush(heap, (nxt, i , j+1))
                
            
            
        