from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        lst = Counter(s).values()
        return len(s)%2 == sum(l%2 for l in lst)