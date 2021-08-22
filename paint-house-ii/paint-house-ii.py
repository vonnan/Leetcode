from heapq import heappush
from heapq import heappop
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        rows, cols = len(costs), len(costs[0])
        dp = [[0]* cols for _ in range(rows)]
        dp[0] = costs[0]
        
        for r in range(1, rows):
            heap = []
            row = dp[r-1]
            for c in range(cols):
                heappush(heap, (row[c], c))
            
            minc, col = heappop(heap)
            for c in range(cols):
                if c!= col:
                    dp[r][c] = minc + costs[r][c]
                else:
                    dp[r][c] = heap[0][0] + costs[r][c]
            
        return min(dp[-1])
        
                
                
        