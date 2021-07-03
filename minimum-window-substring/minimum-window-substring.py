class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dic_t = Counter(t)
        m = len(dic_t)
        
        l, res, ans = 0,inf, ""
        
        seen = set()
        
        dic_s = Counter()
        
        for r, ch in enumerate(s):
            dic_s[ch] += 1
            if ch not in seen and ch in dic_t and dic_s[ch] == dic_t[ch]:
                seen.add(ch)
            
            while len(seen) ==m:
                if s[l] in seen:
                    if dic_s[s[l]] == dic_t[s[l]]:
                        seen.remove(s[l])
                        if res > r - l + 1:
                            res = r - l + 1
                            ans = s[l:r+1]
                dic_s[s[l]] -= 1
                l += 1
                
        return ans
                
                        
                    
                    