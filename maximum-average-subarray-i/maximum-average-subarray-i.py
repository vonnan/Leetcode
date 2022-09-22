class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = max_ = sum(nums[:k])
        for i, num in enumerate(nums[k:], k):
            prefix -= nums[i-k]
            prefix += num
            max_ = max(max_, prefix)
        return max_/k