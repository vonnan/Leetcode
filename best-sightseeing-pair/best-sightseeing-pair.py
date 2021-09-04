class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0]
        res = -inf
        for i, num in enumerate(values[1:], 1):
            res = max(res, num- i + max_i)
            max_i = max(max_i, num + i)
        return res