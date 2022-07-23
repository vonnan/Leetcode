class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo, hi = min(nums), max(nums)
        def check(avg):
            tot = sum(nums[:k]) - avg * k
            if tot >= 0:
                return True
            
            pre, pre_min = 0, 0
            for i in range(k, len(nums)):
                tot += nums[i] - avg
                pre += nums[i - k] - avg
                pre_min = min(pre, pre_min)
                if tot >= pre_min:
                    return True
            
            return False
        
        while hi - lo > 10**(-6):
            mid = (lo + hi)/2
            if check(mid):
                lo = mid
            else:
                hi = mid
        return lo
                
                