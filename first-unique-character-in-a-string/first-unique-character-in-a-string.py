class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        sets =set([ch for ch, val in counter.items() if val ==1])
        if len(sets) == 0:
            return -1
        
        for i, ch in enumerate(s):
            if ch in sets:
                return i
