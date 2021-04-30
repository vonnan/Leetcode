class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted([(s,e) for s,e in slots1 if e-s>= duration])
        slots2 = sorted([(s,e) for s,e in slots2 if e-s>= duration])
        
        for s1,e1 in slots1:
            for s2,e2 in slots2:
                left = max(s1,s2)
                right = min(e1,e2)
                if right - left >= duration:
                    return [left, left + duration]
                
        return []
        