from bisect import bisect_left
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        ages =sorted ([age for age in counter])
        n = len(ages)
        res = 0
        
        presum = [0]
        for age in ages:
            presum.append(counter[age] + presum[-1])
        
        for i in range(n-1, -1, -1):
            lower = 0.5 * ages[i] + 7
            nxt = ceil(lower)
            if nxt == lower:
                nxt += 1
            idx = bisect_left(ages, nxt)
            ct = counter[ages[i]]
            if idx < i:
                res += (presum[i] - presum[idx]) * ct
            
            if ages[i] > 14 and ct > 1:
                res += ct * (ct - 1)
            
        return res
                
            