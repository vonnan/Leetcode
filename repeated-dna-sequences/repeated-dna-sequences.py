class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, seen = set([]), set([])
        
        n = len(s)
        if n <=10:
            return []
        
        for i, c in enumerate(s[:n-9]):
            if s[i:i+10] not in seen:
                seen.add(s[i:i+10])
            else:
                res.add(s[i:i+10])
        return res