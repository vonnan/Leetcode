class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        if not t or not s or (Counter(s) & ct != ct ):
            return ""
        
        cs = Counter()
        
        min_ = inf
        j = 0
        ans = ""
        for i, c in enumerate(s):
            if c in ct:
                cs[c] += 1
                if cs[c] >= ct[c] and (cs & ct == ct):
                    while cs & ct == ct:
                        cs[s[j]] -= 1
                        j += 1
                    j -= 1
                    cs[s[j]] += 1
                    if i - j + 1 < min_:
                        ans = s[j: i + 1]
                        min_ = i - j + 1
        return ans
                    
            