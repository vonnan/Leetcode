class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res, flag = 0, False
        for val in counter.values():
            res += val//2 * 2
            if val % 2:
                flag = True
        return res + 1 if flag else res
        
        