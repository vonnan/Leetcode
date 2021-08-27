class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res, max_idx = 0, 0
        
        for i, val in enumerate(values):
            res = max(res, max_idx + val - i)
            max_idx = max(max_idx, val + i)
            
        return res