class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        res = set([])
        n = len(s)
    
        for i in range(n):
            counter = Counter([])
            for j, c in enumerate(s[i:], i):
                counter[c] += 1
                if len(set(counter.values())) == 1:
                    res.add(s[i: j + 1])
        
        return len(res)