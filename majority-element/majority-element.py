class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_ = max(counter.values())
        for key, val in counter.items():
            if val == max_:
                return key