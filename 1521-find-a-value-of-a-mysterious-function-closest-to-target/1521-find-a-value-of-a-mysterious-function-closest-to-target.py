from bisect import bisect_left

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        res, curr = set([]), set([])
        
        for a in arr:
            curr = {a & b for b in curr} | {a}
            res |= curr
        
        res = sorted(list(res))
        
        idx = bisect_left(res, target)
        if idx ==0:
            return res[0] - target
        elif idx == len(res):
            return target - res[-1]
        else:
            return min(target - res[idx - 1], res[idx] - target)