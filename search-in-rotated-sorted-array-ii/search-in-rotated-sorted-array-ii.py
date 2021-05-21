class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        sets = set(nums)
        return target in sets