class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [ a* num * num + b* num +c for num in nums]
        return sorted(nums)