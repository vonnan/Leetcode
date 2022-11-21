from math import lcm
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        
        for i, num in enumerate(nums):
            l = num
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k:
                    res += 1
                elif l > k:
                    break
        
        return res