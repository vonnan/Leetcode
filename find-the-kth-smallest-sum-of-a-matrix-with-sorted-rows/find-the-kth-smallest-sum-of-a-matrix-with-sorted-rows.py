from heapq import heappush
from heapq import heappop

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row, col = len(mat), len(mat[0])
        
        minimum = sum(mat[i][0] for i in range(row))
        
        heap = [[minimum, "0"* row]]
        visited = set()
        ct = 0
        
        while heap:
            val, idx = heappop(heap)
            ct += 1
            if ct == k:
                return val
            for r in range(row):
                j = int(idx[r])
                new_idx = idx[:r] + str(j+1) + idx[r+1:]
                if (j + 1 < min(col, k)) and new_idx not in visited:
                    heappush(heap, (val + mat[r][j+1] - mat[r][j], new_idx))
                    visited.add(new_idx)
                    
        
        
                    
                    
        
            
                
        