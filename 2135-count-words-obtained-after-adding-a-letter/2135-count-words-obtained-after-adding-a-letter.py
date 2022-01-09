class Solution:
    def wordCount(self, s: List[str], t: List[str]) -> int:
        start = set([])
        a = ord("a")
        for word in s:
            m= 0
            for ch in word:
                m ^= 1 << (ord(ch) - a)
            start.add(m)
            
        res = 0
        for word in t:
            m = 0
            for ch in word:
                m ^= 1 << (ord(ch) - a)
            for ch in word:
                if m ^ (1 << (ord(ch) - a)) in start:
                    res += 1
                    break
        return res