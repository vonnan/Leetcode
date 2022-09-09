class Solution:
    def numSplits(self, s: str) -> int:
        counter = Counter(s)
        
        res = 0
        ct = Counter([])
        
        for i, c in enumerate(s):
            ct[c] += 1
            ct_back = counter - ct
            if len(ct) == len(ct_back):
                res += 1
        return res