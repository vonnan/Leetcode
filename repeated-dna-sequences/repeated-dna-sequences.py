class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s) - 9):
            curr = s[i:i+10]
            if curr in seen and curr not in res:
                res.add(curr)
            elif curr not in seen:
                seen.add(curr)
        return res
        