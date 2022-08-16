class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        sets = set([x for x, val in counter.items() if val == 1])

        if not sets:
            return -1
        
        for i, c in enumerate(s):
            if c in sets:
                return i