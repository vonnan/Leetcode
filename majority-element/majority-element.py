class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max([(v, k) for k,v in counter.items()])[1]