class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, ct, res = 0, 0, 0
        for right, num in enumerate(nums):
            if num == 0:
                ct += 1
                if ct > k:
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    ct -= 1
            res = max(res, right - left + 1)
        return res
                    
                    