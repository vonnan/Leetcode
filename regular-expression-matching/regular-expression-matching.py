class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        if not s:
            return len(p) > 1 and p[1] == "*" and self.isMatch(s, p[2:])
        
        matched = (s[0] == p[0]) or (p[0] == ".")
        
        if len(p) > 1 and p[1] == "*":
            return (matched and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])
                
        return matched and self.isMatch(s[1:], p[1:])
        
        