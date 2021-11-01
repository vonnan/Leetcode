class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        flag = False
        res = 0
        for val in counter.values():
            res += val//2 * 2
            if val % 2:
                flag = True
        return res if not flag else res + 1