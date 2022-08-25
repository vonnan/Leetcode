class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr, cm = Counter(ransomNote), Counter(magazine)
        return all(val <= cm[key] for key, val in cr.items())