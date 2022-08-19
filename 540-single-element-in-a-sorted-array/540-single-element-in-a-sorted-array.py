class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return [key for key, val in counter.items() if val == 1][0]