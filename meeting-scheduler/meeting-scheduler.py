class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slot =[ (s,e) for s,e in slots1 + slots2 if e-s >= duration]
        
        slot.sort()
        
        for i in range(1, len(slot)):
            l1, r1 = slot[i-1]
            l2, r2 = slot[i]
            if r1 >= l2 + duration:
                return [l2, l2 + duration]
            
        return []
            