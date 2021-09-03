class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_r, counter_m = Counter(ransomNote), Counter(magazine)
        if counter_r & counter_m == counter_r:
            return True
        else:
            return False