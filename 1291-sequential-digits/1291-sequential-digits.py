from bisect import bisect_left
from bisect import bisect

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res =[]
        
        for d in range(2, 10):
            res.extend(int("".join([str(x) for x in range(i ,i + d)])) for i in range(1,11 - d))
        
        idx_l = bisect_left(res, low)
        idx_r = bisect(res,high)
        return res[idx_l:idx_r]
                
                