class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        counter= Counter(nums)
        for num, ct in counter.items():
            res += [[num] * i + x for i in range(1, ct +1) for x in res ]
        return res