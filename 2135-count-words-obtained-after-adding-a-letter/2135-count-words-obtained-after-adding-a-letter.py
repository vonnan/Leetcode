class Solution:
    def wordCount(self, s: List[str], t: List[str]) -> int:
        seen = set([])
        
        for word in s:
            m = 0
            for ch in word:
                m ^= 1 << (ord(ch) - ord("a"))
            seen.add(m)
            
        res = 0
        
        for word in t:
            m = 0
            for ch in word:
                m ^= 1 << (ord(ch) - ord("a"))
            
            for ch in word:
                if m ^ 1<<(ord(ch) - ord("a")) in seen:
                    res += 1
                    break
        
        return res