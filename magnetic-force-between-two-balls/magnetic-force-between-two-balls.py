class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        if m == 2:
            return position[-1] - position[0]
        
        left, right, end = 1, position[-1], position[-1]
        
        while left < right:
            mid = (left + right + 1)//2
            start, ct = position[0], 1
            for p in position:
                if p - start < mid:
                    continue
                if p - start >= mid:
                    if end - p >= mid:
                        start = p
                        ct += 1
                    else:
                        ct += 1
                        break
            if ct >= m:
                left = mid
            else:
                right = mid - 1
                    
        return left
                
                        
                
        
                    