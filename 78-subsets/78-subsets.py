class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set([()])
        for num in nums:
            res |= {tuple(list(x) + [num]) for x in res}
            
        return res