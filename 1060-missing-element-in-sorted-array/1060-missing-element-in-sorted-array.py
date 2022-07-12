class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = nums[0]
        for i, num in enumerate(nums[1:], 1):
            if num - prev > k:
                return prev + k
            k -= num - prev -1
            prev = num
        return prev + k
            