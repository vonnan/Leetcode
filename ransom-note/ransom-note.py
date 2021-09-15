class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for c in ransomNote:
            if c not in counter:
                return False
            else:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
        return True