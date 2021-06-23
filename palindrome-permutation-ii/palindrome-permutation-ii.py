from collections import Counter
from itertools import permutations
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def possible(s):
            return len(s)% 2 == sum(x%2 for x in Counter(s).values())
        
        if not possible(s):
            return []
        
        counter = Counter(s)
        c, mid = "", ""
        res = set()
        
        for key, val in counter.items():
            if val%2:
                mid = key
            c += key *(val//2)
            
        for x in permutations(c):
            x = "".join(x)
            res.add(x + mid + x[::-1])
            
        
        return res
            
        