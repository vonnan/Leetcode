from bisect import bisect_left
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sets = set(nums1+ [-inf] + [inf])
        nums = sorted(list(sets))
        lst = [abs(a-b) for a, b in zip(nums1, nums2)]
        
        max_ = 0
        
        for j, num in enumerate(nums2):
            idx = bisect_left(nums, num)
            min_ = min(abs(nums[idx] - num), abs(nums[idx-1] - num))
            if min_ < abs(nums1[j] - num):
                max_ = max(max_, abs(nums1[j] - num) - min_)
        
        return (sum(lst) - max_)% (10** 9 + 7)
        
          
        