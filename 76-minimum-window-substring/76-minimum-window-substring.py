class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct_s, ct_t, res, ans = Counter([]), Counter(t), inf, ""
        seen = set([])
        size, l = len(ct_t), 0
        
        for r, ch in enumerate(s):
            ct_s[ch] += 1
            if ch in ct_t and ct_t[ch] == ct_s[ch]:
                seen.add(ch)
                
            while len(seen) == size:
                if s[l] in ct_t and ct_s[s[l]] == ct_t[s[l]]:
                    seen.remove(s[l])
                    if r- l + 1 < res:
                        res = r - l + 1
                        ans = s[l: r+ 1]
                ct_s[s[l]] -= 1
                l += 1
            
        return ans
                
                    
                