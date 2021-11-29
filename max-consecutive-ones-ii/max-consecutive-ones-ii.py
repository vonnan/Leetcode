class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        zero, n, res  = 0, len(nums), 1
        while right < n:
            if nums[right] == 0:
                zero += 1
                if zero == 2:
                    res = max(right -left, res)
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    zero -= 1
            right += 1
            
        res = max(res, right - left)
        return res
        