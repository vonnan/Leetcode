class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        diff = sorted([stations[i] - stations[i-1]  for i in range(1, len(stations))])
        lo, hi = 0, diff[-1]
        
        while hi - lo > 10**(-6):
            mid = (lo + hi)/ 2
            ct = sum((d-0.0000001)//mid for d in diff)
            
            if ct > k:
                lo = mid + 0.000001
            else:
                hi = mid
        return lo
            
        