
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        sets1, sets2 = set([0]), set([0])
        res, n = abs(goal), len(nums)
        
        for num in nums[:n//2]:
            sets1 |= {num + prev for prev in sets1}
        for num in nums[n//2:]:
            sets2 |= {num + prev for prev in sets2}
        
        sets1, sets2 = sorted(sets1), sorted(sets2)
        n1, n2 = len(sets1), len(sets2)
        
        l, r = 0, n2-1
        while l < n1 and r >=0:
            res = min(res, abs(sets1[l] + sets2[r] - goal))
            if res == 0:
                return 0
            if sets1[l] + sets2[r]> goal:
                r -= 1
            elif sets1[l] + sets2[r] < goal:
                l += 1
        return res
            
        
        
        
        
        