from bisect import bisect
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        lo, hi = 0, max(max(box) for box in boxes) * len(packages)
        packages.sort()
        max_ = packages[-1]
        boxes = [sorted(box) for box in boxes]
        boxes = [ box for box in boxes  if box[-1] >= max_]
        if not boxes:
            return -1
        presum = [0]
        
        for a in packages:
            presum.append(presum[-1] + a)
            
        res = inf
        for box in boxes:
            ct, start = 0, 0
            for b in box:
                nxt = bisect(packages, b, start)
                ct += b * (nxt - start) - (presum[nxt] - presum[start])
                start = nxt
                if ct >= res:
                    break
                
            res = min(ct, res)
        mod = 10 **9 + 7        
        return res % mod
            
            
            
            