class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(zip(counter.values(), counter.keys()))[1]