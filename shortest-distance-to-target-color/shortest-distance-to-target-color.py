from bisect import bisect_left
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dp = [[], [], []]
        for i, c in enumerate(colors):
            dp[c-1].append(i)
        res = []
        for i, c in queries:
            lst = dp[c-1]
            if not lst:
                res.append(-1)
                continue
            idx = bisect_left(lst, i)
            
            if idx == 0:
                res.append(lst[0] - i)
            elif idx == len(lst):
                res.append(i- lst[-1])
            else:
                res.append(min(lst[idx] -i, i - lst[idx-1]))
        return res
        