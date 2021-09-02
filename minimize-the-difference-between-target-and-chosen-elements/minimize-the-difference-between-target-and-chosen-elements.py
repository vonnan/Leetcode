from heapq import heappush
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        bits = 1
        
        for row in mat:
            temp = 0
            for num in row:
                temp |= bits << num
            bits = temp
            
        for d in range(5000):
            if bits >> (target + d) & 1 or d < target and bits >> (target - d) & 1:
                return d
                
               
        
                
        
        
        