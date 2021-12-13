class Solution:
    def maxPower(self, s: str) -> int:
        curr, res = 1, 1
        for i, c in enumerate(s[1:], 1):
            if c == s[i-1]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        return max(res, curr)
                
            