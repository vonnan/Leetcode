from collections import Counter
from itertools import permutations
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def possible(s):
            n = len(s)
            ct = sum(x%2 for x in Counter(s).values())
            return ct -n%2 == 0
        if not possible(s):
            return []
        counter = Counter(s)
        c = ""
        mid = ""
        for key, val in counter.items():
            if val %2:
                mid = key
            c+= key * (val//2)
        
        res = set()
        
        for x in permutations(c):
            x = "".join(x)
            res.add(x+mid+x[::-1])
            
        return res
            
        