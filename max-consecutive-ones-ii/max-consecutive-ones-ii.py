class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        ct, res = 0, 0
        for right, num in enumerate(nums):
            if num == 0:
                ct += 1
                while ct ==2:
                    if nums[left] == 0:
                        ct -= 1
                    left += 1
            res = max(res, right - left + 1)
        return res
                    
        