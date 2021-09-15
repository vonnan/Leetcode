class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        sets =set([key for key, val in counter.items() if val == 1])
        
        if len(sets) ==0:
            return -1
        
        for i, c in enumerate(s):
            if c in sets:
                return i