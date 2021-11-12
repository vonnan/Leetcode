class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        lst = [val + i for i, val in enumerate(values)]
        
        res = -inf
        
        max_ = lst[0]
        
        for j, val in enumerate(values[1:], 1):
            res = max(res, val - j + max_)
            max_ = max(max_, lst[j])
        
        return res