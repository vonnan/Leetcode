
from bisect import bisect_left
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        sets = set(baseCosts)
        for t in toppingCosts:
            for x in list(sets):
                sets.add(x + t)
                sets.add(x + t + t)
        
        lst =sorted(list(sets))
        
        idx = bisect_left(lst, target)
        
        if idx == len(lst):
            return lst[-1]
        
        if idx == 0 or target == lst[idx] or 2* target > lst[idx-1] + lst[idx]:
            return lst[idx]
        
        else:
            return lst[idx-1]
        
            
                
        