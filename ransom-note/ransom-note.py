class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr, cm = Counter(ransomNote), Counter(magazine)
        return cr & cm == cr