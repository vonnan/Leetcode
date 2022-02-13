class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = set([()])
        for num in nums:
            for x in sorted(sets):
                sets.add(tuple([num] + list(x)))
        return sets