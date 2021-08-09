from bisect import insort
from bisect import bisect_left
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = sorted(nums[:k])
        res = []
        m = k//2
        
        def median():
            return lst[m] if k%2 else (lst[m] + lst[m-1])/2
        
        
        for i in range(k, len(nums)):
            res.append(median())
            lst.pop(bisect_left(lst, nums[i - k]))
            insort(lst, nums[i])
        res.append(median())
        
        return res
        