class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        position =[0] + [position[i+1] - position[0] for i in range(n-1)]
        
        left, right = 0, position[-1]
        if m==2:
            return position[-1]
        while left < right:
            mid = (left + right+1)//2
            
            start, ct= 0, 1
            for x in position:
                
                if x - start >= mid:
                    start = x
                    ct += 1
                    if ct > m:
                        break 
            if ct >= m:
                left = mid
            
            else:
                right = mid - 1
            
              
        return left
                
                    
                
            