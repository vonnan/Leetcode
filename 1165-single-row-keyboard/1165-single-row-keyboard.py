class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {c:i for i, c in enumerate(keyboard)}
        
        prev = 0
        res = 0
        
        for c in word:
            nxt = dic[c]
            res += abs(prev - nxt)
            prev = nxt
        
        return res