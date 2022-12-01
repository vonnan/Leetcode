class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        front, back = s[:n//2], s[n//2:]
        
        def ct(s):
            ans = 0
            for c in s:
                if c in "aoieuAOIEU":
                    ans += 1
            return ans
        
        return ct(front) == ct(back)
        
        
        