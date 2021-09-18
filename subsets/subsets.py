class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        res = [[]]
        for num in nums:
            res += [[num] + x for x in res]
            
        return res