class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        tot = 0
        for a, b in shift:
            if a == 1:
                tot += b
            else:
                tot -= b
        
        n = len(s)
        tot %= n
        
        res = s[-tot:] + s[:-tot]
        return res