class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums:
            res.extend([x + [num] for x in res])
        return set([tuple(x) for x in res])
            
