class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sets = set([])
        res = []
        for num in nums:
            if num in sets:
                res.append(num)
            else:
                sets.add(num)
        return res