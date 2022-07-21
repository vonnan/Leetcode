class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        min_, res = nums[k], nums[k]
        n = len(nums)
        
        while left > 0 and right < n-1:
            if nums[left -1] == nums[right + 1]:
                left -= 1
                right += 1
                min_ = min(nums[left], min_)
            elif nums[left -1] > nums[right + 1]:
                left -= 1
                min_ = min(nums[left], min_)
            else:
                right += 1
                min_ = min(nums[right], min_)
            res = max(res, min_ * (right - left + 1))
        
        while left > 0:
            left -= 1
            min_ = min(nums[left], min_)
            res = max(res, min_ * (right - left + 1))
        
        while right < n-1:
            right += 1
            min_ = min(nums[right], min_)
            res = max(res, min_ * (right - left + 1))
            
        return res
                