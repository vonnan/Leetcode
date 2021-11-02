class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        
        n = len(s)
        
        for i in range(n- 9):
            curr = s[i:i+10]
            if curr not in seen:
                seen.add(curr)
            elif curr in seen and curr not in res:
                res.add(curr)
        
        return res