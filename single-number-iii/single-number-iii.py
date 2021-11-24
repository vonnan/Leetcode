class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [x for x, val in counter.items() if val == 1]