class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        else:
            s = list(s)
            while len(s) > 1:
                if s[0] == s[-1]:
                    s.pop(0)
                    s.pop(-1)
                else:
                    break
            
            return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]