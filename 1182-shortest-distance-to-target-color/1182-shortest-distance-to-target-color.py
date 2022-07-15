from bisect import bisect_left
from bisect import bisect

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i, c in enumerate(colors):
            dic[c].append(i)
        
        res = []
        
        for i, c in queries:
            if c not in dic:
                res.append(-1)
            else:
                lst = dic[c]
                if i <= lst[0]:
                    res.append(lst[0] - i)
                elif i >= lst[-1]:
                    res.append(i - lst[-1])
                else:
                    idx = bisect_left(lst, i)
                    res.append(min(lst[idx] - i, i - lst[idx-1]))
        
        return res
            