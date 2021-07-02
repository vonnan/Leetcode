import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        nums.sort()
        
        for i in range(n-1, 1, -1):
            left, right = 0, i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left 
                    right -= 1
                else:
                    left += 1
        return res
        