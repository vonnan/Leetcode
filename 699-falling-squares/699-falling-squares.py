from bisect import bisect
from bisect import bisect_left
from bisect import insort

class Solution:
    def fallingSquares(self, A: List[List[int]]) -> List[int]:
        sets = set([])
        for x, w in A:
            sets.add(x)
            sets.add(x + w)
        lst = sorted(list(sets))
        dic = {num : i for i, num in enumerate(lst)}
        A= [(dic[x], dic[x+w], w) for x, w in A]
        dp = [0] * len(lst)
    
        max_, res = 0, []
        
        for s,e,w in A:
            prev = max(dp[s:e])
            max_ = max(prev + w, max_)
            res.append(max_)
            dp[s: e] = [prev + w] * (e - s)
        
        return res
                
                
            
        