class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], a: int) -> int:
        lst = sorted([(a - b) for a, b in zip(capacity, rocks)], reverse = True)
        
        res = 0
        
        while lst and lst[-1] == 0:
            res += 1
            lst.pop()
        
        while lst and lst[-1] <= a:
            
            a -= lst.pop()
            res += 1
        
        return res
            
        