class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sets = set(list(range(1, n + 1)))
        
        return sets - set(nums)