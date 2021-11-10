class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res = sum([x//2*2 for x in counter.values()])
        if sum([x%2 for x in counter.values()]):
            res += 1
        return res
        