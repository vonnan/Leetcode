class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        counter = Counter(s)
        for word in words:
            start = 0
            flag = True
            ct = Counter(word)
            if ct & counter != ct:
                continue
            for c in word:
                if c not in s[start:]:
                    flag = False
                    break
                else:
                    start = s.index(c, start) + 1
            if flag:
                res += 1
        return res
            
                