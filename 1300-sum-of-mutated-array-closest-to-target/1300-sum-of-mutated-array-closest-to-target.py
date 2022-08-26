from bisect import bisect

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        presum = list(accumulate(arr, initial = 0))
        left, right = 0, arr[-1]
        
        def helper(m):
            idx = bisect(arr, m)
            return presum[idx] + (n - idx) * m
        
        if presum[-1] <= target:
            return arr[-1]
        res = right
        
        while left <= right:
            mid = (left + right + 1) //2
            
            tot = helper(mid)
            
            if tot == target:
                return mid
            elif tot > target:    
                right = mid - 1
            else:
                left = mid + 1
            
        
        if abs(helper(left) - target) < abs(helper(right) - target):
            return left
        return right
        
            
        
            
