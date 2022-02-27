from bisect import bisect_left

class Solution:
    def minimumTime(self, time: List[int], A: int) -> int:
        time.sort()
        left, right = 1, A * time[0] 
        while left < right:
            mid = (left + right)//2
            
            ct = sum( mid// t for t in time if t <= mid)
            if ct >= A:
                right = mid
            else:
                left = mid + 1
        return left
             
            
            
            
        
        
            
        
            
            
        