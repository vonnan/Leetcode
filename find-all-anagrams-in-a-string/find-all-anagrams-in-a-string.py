class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        res = []
        n, m = len(p), len(s)
        presum = Counter(s[:n])
        if presum == counter:
            res.append(0)
           
        for i in range(1, m-n+1):
            c = s[i+n-1]
            presum[c] += 1
            presum[s[i-1]] -= 1
            
            if presum[s[i-1]] ==0:
                del presum[s[i-1]]
            
            if c in counter and presum == counter:
                res.append(i)
            
        return res