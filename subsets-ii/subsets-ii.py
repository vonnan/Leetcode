class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num, freq in Counter(nums).items():
            res += [r + [num] * i for r in res for i in range(1, freq + 1)]
        return res