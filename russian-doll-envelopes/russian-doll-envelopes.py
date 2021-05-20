from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        res = []
        for w,h in envelopes:
            idx = bisect_left(res, h)
            if idx == len(res):
                res.append(h)
            else:
                res[idx] = h
        return len(res)