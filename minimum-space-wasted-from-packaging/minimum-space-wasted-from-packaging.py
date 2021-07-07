from bisect import bisect
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        tot, maxP = sum(packages), max(packages)
        res, mod = inf, 10**9 +7
        for box in boxes:
            box.sort()
            if box[-1] < maxP:
                continue
            ct, start = 0, 0
            for b in box:
                idx = bisect(packages, b, start)
                ct += b*(idx - start)
                start = idx
                if ct > res:
                    break
            res = min(res, ct)
        return (res - tot)% mod if res != inf else -1