class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        counter = Counter(nums)
        for num, f in sorted(counter.items()):
            res += [x + [num] * i  for x in res for i in range(1, f + 1)]
        return res
