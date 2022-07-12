class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        counter = Counter(nums)
        n = len(nums)
        return counter[target]* 2 > n