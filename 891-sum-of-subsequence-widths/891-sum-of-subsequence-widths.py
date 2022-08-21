class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        n = len(nums)
        return sum(((1<<i) - (1<<(n-1-i))) * num % mod for i, num in enumerate(nums)) % mod