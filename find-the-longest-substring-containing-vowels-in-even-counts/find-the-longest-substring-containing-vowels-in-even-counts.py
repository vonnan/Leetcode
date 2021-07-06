class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        memo = {0: 0}
        
        curr, res = 0, 0
        
        for i, ch in enumerate(s,1):
            if ch in dic:
                curr ^= 1 << dic[ch]
            if curr in memo:
                res = max(res, i - memo[curr])
            else:
                memo[curr] = i
        
        return res