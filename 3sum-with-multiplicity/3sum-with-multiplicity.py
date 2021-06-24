from collections import Counter
from itertools import combinations_with_replacement

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ct, res = Counter(arr), 0
        for a,b in combinations_with_replacement(ct, 2):
            c = target - a - b
            if c not in ct:
                continue
            print(a,b, c)
            if a == b == c:
                res += ct[a]*(ct[a]-1)*(ct[a]-2)//6
            elif a == b != c:
                res += ct[a] * (ct[a] -1)//2 * ct[c]
            elif c > a and c > b: 
                res += ct[a] *ct[b]* ct[c]
       
        return res%(10**9+7)
        
                    
                
            