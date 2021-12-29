class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        zero, res = 0, 0
        
        for right, num in enumerate(nums):
            if num == 0:
                zero += 1
                if zero == 2:
                    res = max(res, right -left)
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    zero -= 1
            res = max(res, right - left + 1)
        return res