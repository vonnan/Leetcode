class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slot =[(s,e) for s,e in slots1 + slots2 if e - s >= duration]
        slot.sort()
        
        for i in range(len(slot)-1):
            s1,e1 = slot[i]
            s2, e2 = slot[i+1]
            if e1 >= s2 + duration:
                return [s2, s2+ duration]
            
        return []
        
        