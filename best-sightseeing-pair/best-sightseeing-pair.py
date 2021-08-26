class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, max_i = 0, 0
        for i, a in enumerate(values):
            res = max(res, max_i + a - i)
            max_i = max(max_i, a + i)
        return res