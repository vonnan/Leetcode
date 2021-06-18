from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ct = sum(x%2 for x in Counter(s).values())
        n = len(s)
        if ct - n%2 >0:
            return False
        else:
            return True