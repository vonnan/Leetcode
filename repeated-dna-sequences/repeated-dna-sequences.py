class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set([])
        
        seen = set([])
        
        if len(s) <= 10:
            return res
        
        n = len(s)
        for i in range(n - 9):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return res