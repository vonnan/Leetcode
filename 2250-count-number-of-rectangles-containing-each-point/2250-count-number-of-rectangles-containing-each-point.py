from bisect import bisect
from bisect import bisect_left

class Solution:
    def countRectangles(self, A: List[List[int]], points: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        A.sort()
        for x,y in A:
            dic[y].append(x)
        
        def contains(x, y):
            ct = 0
            for yi, lst in dic.items():
                n = len(lst)
                if y <= yi:
                    ct += n - bisect_left(lst, x)
            return ct
        res = []
        for x,y in points:
            res.append(contains(x,y))
        return res
            
        
        
        