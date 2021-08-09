from bisect import insort
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lst = sorted(nums[:k])
        
        res = []
        m = k//2
        
        def median(lst):
            if k % 2:
                res.append(lst[m])
            else:
                res.append((lst[m] + lst[m-1])/2)
        
        median(lst)
        
        for i in range(1, len(nums) - k +1):
            lst.remove(nums[i - 1])
            insort(lst, nums[i + k - 1])
            median(lst)
        
        return res
        