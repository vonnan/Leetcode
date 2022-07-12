class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        return sum(val//2 * 2 for val in counter.values() if val > 1) + any(val%2 for val in counter.values())
        
        