class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        row, col = len(s), len(t)
        
        def helper(r, c):
            prev = curr = res = 0
            for k in range(min(row - r, col - c)):
                curr += 1
                if s[r+k] != t[c+k]:
                    prev, curr = curr, 0
                res += prev
            return res
        
        return sum(helper(r,0) for r in range(row)) + sum(helper(0,c) for c in range(1, col))