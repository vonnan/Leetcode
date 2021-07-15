
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        missing = [num - nums[0] - i for i, num in enumerate(nums)]
        
        if k > missing[-1]:
            return nums[-1] + k - missing[-1]
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi)//2
            if missing[mid] < k:
                lo = mid +1
            else:
                hi = mid
        return nums[lo -1] + k - missing[lo - 1]
                