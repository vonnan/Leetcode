class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        m, n = len(slots1), len(slots2)
        i, j = 0, 0
        slots1.sort()
        slots2.sort()
        
        while i < m and j < n:
            l1,r1 = slots1[i]
            l2,r2 = slots2[j]
            
            left = max(l1,l2)
            
            if r1 < r2:
                i += 1
                if left + duration <= r1:
                    return [left, left + duration]
                
            else:
                j += 1
                if left + duration <= r2:
                    return [left, left + duration]
                
        return []
        
        