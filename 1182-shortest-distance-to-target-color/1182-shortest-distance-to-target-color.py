from bisect import bisect_left
from bisect import bisect
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i, c in enumerate(colors):
            dic[c].append(i)
        print(dic)
        res = []
        for i, c in queries:
            if c not in dic:
                res.append(-1)
            else:
                idx = bisect_left(dic[c], i)
                if idx == 0:
                    res.append(dic[c][0] - i)
                elif idx == len(dic[c]):
                    res.append(i - dic[c][-1])
                else:
                    res.append(min(dic[c][idx] - i, i - dic[c][idx - 1]))
        
        return res