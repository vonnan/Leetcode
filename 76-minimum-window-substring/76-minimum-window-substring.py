class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct_s, ct_t, res = Counter(), Counter(t), inf
        left, seen = 0, set([])
        ans = ""
        
        for right, c in enumerate(s):
            ct_s[c] += 1
            if c in ct_t and ct_s[c] == ct_t[c]:
                seen.add(c)
                        
            while len(seen) == len(ct_t):
                if s[left] in ct_t and ct_s[s[left]] == ct_t[s[left]]:
                    seen.remove(s[left])
                    if right - left + 1 < res:
                        res = right - left + 1
                        ans = s[left: right + 1]
                
                ct_s[s[left]] -= 1
                left += 1
        
        return ans
                
                    
                    
                    
                    
                    
                    
                