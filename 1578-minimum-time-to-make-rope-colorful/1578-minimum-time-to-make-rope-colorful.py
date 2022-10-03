from bisect import insort

class Solution:
    def minCost(self, colors: str, A: List[int]) -> int:
        res = sum(A)
        
        prev, max_ = colors[0], A[0]
        
        for c, t in zip(colors[1:], A[1:]):
            if c == prev:
                max_= max(max_, t)
            else:
                res -= max_
                max_ = t
            prev = c
        
        return res - max_
                
                
                    
                