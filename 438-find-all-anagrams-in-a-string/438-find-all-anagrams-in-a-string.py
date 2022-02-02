class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        n, ct, res, prev = len(p), Counter(), [], -1
        for i,c in enumerate(s):
            if c not in counter:
                ct = Counter()
                prev = i
            else:
                ct[c] += 1
                while ct[c] > counter[c]:
                    ct[s[prev+1]] -= 1
                    prev += 1
                if ct == counter:
                    res.append(i-n+1)
            
        return res
                
            