class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        score, res = 0, 0
        seen = {}
        
        for i, hour in enumerate(hours):
            if hour > 8:
                score += 1
            else:
                score -= 1
                
            if score > 0:
                res = i + 1
                
            else:
                if score not in seen:
                    seen[score] = i
                if score - 1 in seen:
                    res = max(res, i - seen[score - 1])
                    
        return res