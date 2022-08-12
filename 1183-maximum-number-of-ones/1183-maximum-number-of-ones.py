from math import ceil

class Solution:
    def maximumNumberOfOnes(self, row: int, col: int, L: int, max_: int) -> int:
        if not max_:
            return 0
        
        if max_ == L * L:
            return row * col
        
        res = []
        for r in range(L):
            for c in range(L):
                res.append(ceil((row-r)/L) * ceil((col - c)/ L))
                
        res.sort()
        return sum(res[-max_:])
        
        
        
        