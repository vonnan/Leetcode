class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct_t, ct_s, res = Counter(t), Counter(), inf
        seen, size, l, ans = set(), len(ct_t), 0, ""
        
        for r, ch in enumerate(s):
            ct_s[ch] += 1
            #counter of t of ch adds 1
            if ch in ct_t and ct_t[ch] == ct_s[ch]:
                seen.add(ch)
            #if ct_t[ch] == ct_s[ch], add ch to seen
            
            while len(seen) == size:
                if ct_t[s[l]] == ct_s[s[l]]:
                    #make the left side as "compact" as possible: if the leftmost character can not be removed, it the "shortest" we can get with the rightmost position as r
                    seen.remove(s[l])
                    if res > r - l + 1:
                        res = r - l + 1
                        ans = s[l:r+1]
                ct_s[s[l]] -= 1
                l += 1
        
        return ans
            
    