from bisect import bisect
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        tot, res, mod = sum(packages), inf, 10**9 + 7
        
        for box in boxes:
            box.sort()
            if box[-1] < packages[-1]:
                continue
            start, ct = 0, 0
            for b in box:
                idx = bisect(packages, b, start)
                ct += (idx - start)*b
                start = idx
                if ct > res:
                    break
            res = min(res, ct)
        return (res- tot) % mod if res != inf else -1
        