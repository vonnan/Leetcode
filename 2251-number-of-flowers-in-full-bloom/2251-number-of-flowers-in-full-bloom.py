from bisect import bisect
from bisect import bisect_left
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = defaultdict(int)
        for s,e in flowers:
            diff[s] += 1
            diff[e+1] -= 1
        diff[0] = 0    
        prev = 0
        lst = sorted(list(diff.keys()))
        for key in lst:
            diff[key] += diff[prev]
            prev = key
        
        return [diff[lst[bisect(lst, d)-1]] for d in persons]
        
            
            
            