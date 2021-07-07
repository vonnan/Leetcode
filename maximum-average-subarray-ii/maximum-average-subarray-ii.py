class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo, hi = min(nums), max(nums)
        
        def check(avg):
            tot = sum(nums[:k]) - avg * k
            if tot >= 0:
                return True
            prev, prev_min =0 ,0
            for i in range(k, len(nums)):
                tot += nums[i] - avg
                prev += nums[i-k] - avg
                prev_min = min(prev, prev_min)
                if tot >= prev_min:
                    return True
                
            return False
        
        while hi - lo > 10**(-6):
            mid = (hi + lo)/2
            if check(mid):
                lo = mid
            else:
                hi = mid
                
        return lo
            
            